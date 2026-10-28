# coding: utf-8
 
# # AI-Powered US Real Estate Market Intelligence Platform
# ### Market sentiment, topic analysis, risk signals and a Real Estate Sentiment Index (RESI)
# 
# **Dataset:** Real estate market sentiment posts (Reddit, Lemmy, Bluesky, Mastodon, YouTube, ...)
# **Goal:** Turn raw social-media text into signals that investors, REALTORS and mortgage teams can use.
# 
# **What this notebook covers (follows the Task 2 roadmap):**
# 
# | Step | Section |
# |---|---|
# | 1 | Load and clean the data |
# | 2 | Sentiment distribution and class imbalance |
# | 3 | NLP analysis: word frequency, n-grams, topic modeling |
# | 4 | Feature engineering |
# | 5 | Model building: Logistic Regression, Random Forest, XGBoost, LightGBM |
# | 6 | Handling imbalance: class weights vs SMOTE |
# | 7 | Explainable AI: top words and SHAP |
# | 8 | Real Estate Sentiment Index (RESI), trend and early warning system |
# | 9 | Market risk traffic light |
# | 10 | Investor dashboard |
# | 11 | Save the model and a reusable `predict_sentiment()` function |
# 
# **How to run:** put this file next to the CSV and run it. In Jupyter use `Kernel > Restart & Run All`; as a plain Python script run `python Real_estate_data.py` from the folder that contains the CSV.
 
# ## 0. Setup
 
# In[1]:
 
 
import os
import re
import time
import warnings
 
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse import csr_matrix, hstack
 
from sklearn.decomposition import LatentDirichletAllocation, NMF
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.utils.class_weight import compute_sample_weight
 
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from imblearn.over_sampling import SMOTE
from textblob import TextBlob
import shap
 
try:
    from IPython.display import display      # nice tables inside Jupyter / VS Code notebooks
except ImportError:
    display = print                           # plain Python script: just print the table
 
warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.dpi"] = 110
pd.set_option("display.width", 200)          # show full tables when running as a script
pd.set_option("display.max_columns", 30)
 
# ----- Project settings (change these if needed) -----
DATA_PATH = "Project 2/real_estate_market_sentiment__2026-09-18__de7a8d4a.csv"
OUTPUT_DIR = "outputs"
RANDOM_STATE = 42
TIME_SERIES_START = "2025-01-01"   # before this date the data has only a handful of posts per year
MIN_POSTS_PER_MONTH = 20      # months with fewer relevant posts are too noisy for an index
RESI_SMOOTHING = 5            # pseudo-count that stops tiny months from producing extreme index values
 
os.makedirs(OUTPUT_DIR, exist_ok=True)
 
 
def save_and_show(name):
    """Save the current figure into the outputs folder, then display it."""
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"{name}.png"), bbox_inches="tight")
    plt.show()
 
 
# ## 1. Load the data
# 
# The file has 334 columns, but most are empty "enrichment" columns from other topics (gaming, health, crypto...).
# We only load the columns this project actually needs, which is faster and easier to read.
 
# In[2]:
 
 
USE_COLS = [
    "id", "platform", "published_at", "content",
    "sentiment_label", "sentiment_score",                    # sentiment (produced by the VADER lexicon)
    "is_spam", "language_detected",                          # used for cleaning
    "crisis_signal", "financial_signal",                     # used for the risk score
]
 
df_raw = pd.read_csv(DATA_PATH, usecols=USE_COLS, low_memory=False)
print(f"Rows: {df_raw.shape[0]:,} | Columns loaded: {df_raw.shape[1]}")
display(df_raw.head(3))
 
 
# ## 2. Clean the data
# 
# A first look showed that the file is **not** 100% real estate text. It also contains crypto price tickers
# (`Pair: COST/USDG ...`), image-only markdown posts, spam, and general news. Training on that would add noise,
# so we apply these steps and print how many rows each one removes:
# 
# 1. Drop rows without a date or text
# 2. Drop crypto price-ticker rows (`Pair: ...`)
# 3. Drop spam and non-English posts
# 4. Clean the text (remove links, images, symbols, numbers)
# 5. Drop posts that are too short to carry meaning
# 6. Keep only posts that mention real-estate topics (keyword filter)
 
# In[3]:
 
 
REAL_ESTATE_KEYWORDS = (
    r"real estate|housing|mortgage|home price|home value|homeowner|homebuyer|home buyer|home sale|home loan|"
    r"home equity|\brent\b|rental|property|properties|realtor|zillow|redfin|landlord|tenant|\breit|"
    r"interest rate|inventory|foreclos|cap rate|multifamily|\bhoa\b|vacan|apartment|condo|"
    r"commercial real|first-time buyer|affordab|square met|office space"
)
 
 
def clean_text(text):
    """Lowercase text and remove markdown images/links, URLs, numbers and symbols."""
    text = re.sub(r"!?\[[^\]]*\]\([^)]*\)", " ", text)   # markdown links and images
    text = re.sub(r"http\S+|www\.\S+", " ", text)         # plain URLs
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)                  # keep letters only
    return re.sub(r"\s+", " ", text).strip()
 
 
cleaning_log = []
 
 
def log_step(step_name, data):
    cleaning_log.append({"step": step_name, "rows_left": len(data)})
 
 
df = df_raw.copy()
log_step("Raw data", df)
 
# 1. valid date and text
# Dates come in two ISO formats (with and without microseconds). format="ISO8601" reads both;
# without it, pandas guesses the format from the first row and silently turns the other rows into missing dates.
df["published_at"] = pd.to_datetime(df["published_at"], format="ISO8601", errors="coerce", utc=True).dt.tz_localize(None)
df = df.dropna(subset=["published_at", "content"])
log_step("1. Has date and text", df)
 
# 2. crypto price tickers
df = df[~df["content"].str.startswith("Pair:")]
log_step("2. Remove crypto 'Pair:' rows", df)
 
# 3. spam and language
df = df[(~df["is_spam"]) & (df["language_detected"] == "en")]
log_step("3. Remove spam / non-English", df)
 
# 4. clean text
df["clean_text"] = df["content"].apply(clean_text)
 
# 5. too short (image-only posts become empty after cleaning)
df = df[df["clean_text"].str.len() >= 15]
log_step("4-5. Remove very short / image-only posts", df)
 
# 6. real-estate relevance
is_relevant = df["content"].str.contains(REAL_ESTATE_KEYWORDS, case=False, regex=True)
df = df[is_relevant].reset_index(drop=True)
log_step("6. Keep real-estate related posts", df)
 
display(pd.DataFrame(cleaning_log))
 
 
# ## 3. Sentiment distribution
# 
# Questions from the roadmap: *Is sentiment balanced? Are negative samples under-represented? Is the dataset biased?*
 
# In[4]:
 
 
order = ["negative", "neutral", "positive"]
counts = df["sentiment_label"].value_counts().reindex(order)
percent = (counts / counts.sum() * 100).round(1)
display(pd.DataFrame({"posts": counts, "percent": percent}))
 
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
 
# left: class distribution
colors = {"negative": "#d1495b", "neutral": "#8d99ae", "positive": "#2a9d8f"}
sns.barplot(x=counts.index, y=counts.values, palette=colors, ax=axes[0])
axes[0].set_title("Sentiment distribution")
axes[0].set_xlabel("")
axes[0].set_ylabel("Number of posts")
for i, v in enumerate(counts.values):
    axes[0].text(i, v, f"{v:,}", ha="center", va="bottom")
 
# right: sentiment mix per platform
mix = pd.crosstab(df["platform"], df["sentiment_label"], normalize="index")[order] * 100
mix.plot(kind="barh", stacked=True, color=[colors[c] for c in order], ax=axes[1])
axes[1].set_title("Sentiment mix by platform (%)")
axes[1].set_xlabel("%")
axes[1].set_ylabel("")
axes[1].legend(title="", loc="lower right")
save_and_show("01_sentiment_distribution")
 
ratio = counts["neutral"] / counts["negative"]
print(f"Neutral posts outnumber negative posts {ratio:.1f} to 1 -> the dataset is imbalanced.")
 
 
# **Reading this:** most posts are neutral, and negative posts are the smallest class. A model trained
# naively will learn to predict "neutral" almost every time and look accurate while missing the bearish posts
# that investors care about most. That is why we use **macro F1** (average of per-class F1) instead of plain
# accuracy, and why section 6 tests class weights and SMOTE.
 
# ## 4. NLP analysis
# 
# ### 4.1 Word frequency and n-grams
# We remove common English stop words and a few web words (`https`, `com`, ...) so the real-estate vocabulary stands out.
 
# In[5]:
 
 
EXTRA_STOP_WORDS = {"https", "http", "www", "com", "org", "amp", "just", "like", "don", "ve", "ll", "really", "going", "year", "years", "new"}
STOP_WORDS = list(ENGLISH_STOP_WORDS.union(EXTRA_STOP_WORDS))
 
 
def top_terms(texts, ngram_range=(1, 1), top_n=15, min_df=3):
    """Return the most frequent words / phrases as a pandas Series."""
    vectorizer = CountVectorizer(stop_words=STOP_WORDS, ngram_range=ngram_range, min_df=min_df)
    matrix = vectorizer.fit_transform(texts)
    frequency = np.asarray(matrix.sum(axis=0)).ravel()
    return pd.Series(frequency, index=vectorizer.get_feature_names_out()).sort_values(ascending=False).head(top_n)
 
 
words = top_terms(df["clean_text"], (1, 1))
bigrams = top_terms(df["clean_text"], (2, 2))
trigrams = top_terms(df["clean_text"], (3, 3), min_df=2)
 
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
for ax, series, title in zip(axes, [words, bigrams, trigrams], ["Top words", "Top bigrams (2 words)", "Top trigrams (3 words)"]):
    sns.barplot(x=series.values, y=series.index, color="#457b9d", ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Frequency")
save_and_show("02_top_terms")
 
 
# ### 4.2 Key economic terms by sentiment
# The roadmap highlights inflation, mortgage, interest rate, demand, inventory, construction and affordability.
# For each term: how many posts mention it, and what share of those posts are negative / positive?
 
# In[6]:
 
 
KEY_TERMS = ["inflation", "mortgage", "interest rate", "demand", "inventory", "construction", "affordab", "foreclos", "rent"]
 
rows = []
for term in KEY_TERMS:
    mentions = df["clean_text"].str.contains(rf"\b{term}", regex=True)
    subset = df[mentions]
    rows.append({
        "term": term,
        "posts": len(subset),
        "% negative": round((subset["sentiment_label"] == "negative").mean() * 100, 1),
        "% positive": round((subset["sentiment_label"] == "positive").mean() * 100, 1),
    })
 
key_terms_table = pd.DataFrame(rows).set_index("term").sort_values("posts", ascending=False)
overall = {
    "% negative": round((df["sentiment_label"] == "negative").mean() * 100, 1),
    "% positive": round((df["sentiment_label"] == "positive").mean() * 100, 1),
}
print(f"Baseline for all posts -> negative: {overall['% negative']}% | positive: {overall['% positive']}%")
display(key_terms_table)
 
 
# Compare each row with the baseline above. A term whose `% negative` is clearly higher than the baseline is a
# **bearish topic**; a higher `% positive` marks a **bullish topic**.
 
# ### 4.3 Topic modeling (LDA and NMF)
# Topic modeling groups posts by the words that appear together. We try two classic methods:
# 
# * **LDA** (works on word counts)
# * **NMF** (works on TF-IDF weights, usually gives cleaner topics on short text)
# 
# BERTopic is a good next step, but it needs a transformer model download, so we keep this notebook lightweight.
 
# In[7]:
 
 
N_TOPICS = 5
 
 
def show_topics(model, feature_names, top_n=8):
    """Print the top words of each topic."""
    for topic_id, weights in enumerate(model.components_):
        top_words = [feature_names[i] for i in weights.argsort()[::-1][:top_n]]
        print(f"Topic {topic_id}: {', '.join(top_words)}")
 
 
# --- LDA ---
count_vec = CountVectorizer(stop_words=STOP_WORDS, max_df=0.5, min_df=5, max_features=3000)
count_matrix = count_vec.fit_transform(df["clean_text"])
lda = LatentDirichletAllocation(n_components=N_TOPICS, random_state=RANDOM_STATE, learning_method="batch")
lda.fit(count_matrix)
print("LDA topics")
show_topics(lda, count_vec.get_feature_names_out())
 
# --- NMF ---
tfidf_topic = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5, min_df=5, max_features=3000)
tfidf_topic_matrix = tfidf_topic.fit_transform(df["clean_text"])
nmf = NMF(n_components=N_TOPICS, random_state=RANDOM_STATE, init="nndsvd", max_iter=400)
doc_topic = nmf.fit_transform(tfidf_topic_matrix)
print("\nNMF topics")
show_topics(nmf, tfidf_topic.get_feature_names_out())
 
 
# In[8]:
 
 
# Give each NMF topic a readable name (edit these after reading the words above).
TOPIC_NAMES = {
    0: "DSCR / refinance loans",
    1: "Mortgage rates & loans",
    2: "Real estate investing",
    3: "Home prices, rent & buyers",
    4: "Multifamily & tax strategy",
}
 
df["topic"] = pd.Series(doc_topic.argmax(axis=1)).map(TOPIC_NAMES)
 
topic_summary = (
    df.groupby("topic")
      .agg(posts=("id", "size"),
           pct_negative=("sentiment_label", lambda s: round((s == "negative").mean() * 100, 1)),
           pct_positive=("sentiment_label", lambda s: round((s == "positive").mean() * 100, 1)))
      .sort_values("posts", ascending=False)
)
display(topic_summary)
 
 
# ## 5. Feature engineering
# 
# Besides the TF-IDF text features, we add simple numeric features that describe each post:
# length, word counts from small positive / negative real-estate word lists, punctuation, readability, and TextBlob polarity.
# 
# > **Avoiding data leakage:** the labels in this file come from the VADER lexicon. So we do **not** use the
# > columns `sentiment_score`, `sentiment_positive`, `sentiment_negative`, or `sentiment_confidence` as inputs;
# > they would simply give the answer away. TextBlob uses a different lexicon, so it is a legitimate extra signal.
 
# In[9]:
 
 
POSITIVE_WORDS = {"good", "growth", "strong", "profit", "demand", "gain", "rise", "opportunity",
                  "affordable", "recovery", "boom", "increase", "great", "best", "success"}
NEGATIVE_WORDS = {"crisis", "fall", "decline", "inflation", "recession", "crash", "drop", "risk",
                  "loss", "expensive", "bubble", "foreclosure", "bad", "worst", "debt", "fear"}
 
NUMERIC_FEATURES = [
    "char_count", "word_count", "avg_word_length",
    "positive_word_count", "negative_word_count",
    "exclamation_count", "question_count",
    "textblob_polarity", "textblob_subjectivity", "readability",
]
 
 
def count_syllables(word):
    """Rough syllable count: number of vowel groups (good enough for a readability score)."""
    return max(1, len(re.findall(r"[aeiouy]+", word)))
 
 
def flesch_reading_ease(text):
    """Flesch reading ease: higher = easier to read. Simple version that needs no extra libraries."""
    words = text.split()
    if not words:
        return 0
    sentences = max(1, len(re.findall(r"[.!?]+", text)))
    syllables = sum(count_syllables(w) for w in words)
    return 206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syllables / len(words))
 
 
def extract_features(raw_texts):
    """Turn raw post text into a table of numeric features (used for training AND for new predictions)."""
    raw_texts = pd.Series(raw_texts).reset_index(drop=True)
    cleaned = raw_texts.apply(clean_text)
    tokens = cleaned.str.split()
 
    features = pd.DataFrame(index=raw_texts.index)
    features["char_count"] = cleaned.str.len()
    features["word_count"] = tokens.str.len()
    features["avg_word_length"] = features["char_count"] / features["word_count"].clip(lower=1)
    features["positive_word_count"] = tokens.apply(lambda t: sum(w in POSITIVE_WORDS for w in t))
    features["negative_word_count"] = tokens.apply(lambda t: sum(w in NEGATIVE_WORDS for w in t))
    features["exclamation_count"] = raw_texts.str.count("!")
    features["question_count"] = raw_texts.str.count(r"\?")
    features["textblob_polarity"] = cleaned.apply(lambda t: TextBlob(t).sentiment.polarity)
    features["textblob_subjectivity"] = cleaned.apply(lambda t: TextBlob(t).sentiment.subjectivity)
    features["readability"] = raw_texts.apply(flesch_reading_ease).clip(-100, 120)   # limit extreme outliers
    return features[NUMERIC_FEATURES]
 
 
feature_table = extract_features(df["content"])
display(feature_table.describe().T.round(2))
 
 
# In[10]:
 
 
# Do the new features differ between sentiment classes? (average per class)
display(feature_table.groupby(df["sentiment_label"].values).mean().T.round(2)[order])
 
 
# ## 6. Build and compare models
# 
# **Plan**
# 1. Split the data 80% train / 20% test (stratified, so each set keeps the same class mix)
# 2. TF-IDF on the text (words and 2-word phrases) + scaled numeric features
# 3. Train four models of increasing complexity, all handling imbalance with class weights
# 4. Compare them with **macro F1** (fair to the small negative class)
 
# In[11]:
 
 
# --- 1. labels and split ---
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df["sentiment_label"])          # negative=0, neutral=1, positive=2
class_names = list(label_encoder.classes_)
 
train_idx, test_idx = train_test_split(
    np.arange(len(df)), test_size=0.2, stratify=y, random_state=RANDOM_STATE
)
y_train, y_test = y[train_idx], y[test_idx]
 
# --- 2. text + numeric features (fit on TRAIN only, then apply to TEST) ---
tfidf = TfidfVectorizer(stop_words=STOP_WORDS, ngram_range=(1, 2), min_df=3, max_features=3000)
scaler = MinMaxScaler()
 
X_text_train = tfidf.fit_transform(df.loc[train_idx, "clean_text"])
X_text_test = tfidf.transform(df.loc[test_idx, "clean_text"])
 
X_num_train = scaler.fit_transform(feature_table.iloc[train_idx])
X_num_test = scaler.transform(feature_table.iloc[test_idx])
 
X_train = hstack([X_text_train, csr_matrix(X_num_train)]).tocsr()
X_test = hstack([X_text_test, csr_matrix(X_num_test)]).tocsr()
feature_names = list(tfidf.get_feature_names_out()) + NUMERIC_FEATURES
 
print(f"Train: {X_train.shape} | Test: {X_test.shape}")
print("Train class mix:", dict(zip(class_names, np.bincount(y_train))))
 
 
# In[12]:
 
 
# --- 3. define the models ---
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, class_weight="balanced"),
    "Random Forest": RandomForestClassifier(n_estimators=300, class_weight="balanced_subsample",
                                            n_jobs=-1, random_state=RANDOM_STATE),
    "XGBoost": XGBClassifier(n_estimators=300, max_depth=6, learning_rate=0.1,
                             eval_metric="mlogloss", n_jobs=-1, random_state=RANDOM_STATE),
    "LightGBM": LGBMClassifier(n_estimators=300, learning_rate=0.1, class_weight="balanced",
                               random_state=RANDOM_STATE, verbose=-1),
}
 
# --- 4. train and evaluate ---
results, fitted_models, predictions = [], {}, {}
 
for name, model in models.items():
    start = time.time()
    if name == "XGBoost":
        # XGBoost has no class_weight option, so we pass balanced sample weights instead
        model.fit(X_train, y_train, sample_weight=compute_sample_weight("balanced", y_train))
    else:
        model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
 
    fitted_models[name] = model
    predictions[name] = y_pred
    results.append({
        "model": name,
        "accuracy": accuracy_score(y_test, y_pred),
        "macro_f1": f1_score(y_test, y_pred, average="macro"),
        "negative_recall": recall_score(y_test, y_pred, labels=[0], average=None)[0],
        "seconds": time.time() - start,
    })
 
results_table = pd.DataFrame(results).set_index("model").sort_values("macro_f1", ascending=False).round(3)
display(results_table)
 
 
# In[13]:
 
 
best_name = results_table.index[0]
best_model = fitted_models[best_name]
print(f"Best model by macro F1: {best_name}\n")
print(classification_report(y_test, predictions[best_name], target_names=class_names, digits=3))
 
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
 
results_table["macro_f1"].sort_values().plot(kind="barh", color="#457b9d", ax=axes[0])
axes[0].set_title("Model comparison (macro F1)")
axes[0].set_xlabel("Macro F1")
axes[0].set_ylabel("")
 
cm = confusion_matrix(y_test, predictions[best_name])
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names, ax=axes[1])
axes[1].set_title(f"Confusion matrix: {best_name}")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")
save_and_show("03_model_comparison")
 
 
# > **Important note about these scores.** The sentiment labels in this dataset were created automatically by the
# > VADER lexicon (the `sentiment_method` column says `vader_lexicon`). So these models are mostly learning to
# > *reproduce VADER's rules*, and high scores do not automatically mean they understand real estate sentiment.
# > That is normal for a learning project, but for a client-ready product the next step is to re-label a sample
# > by hand (or with FinBERT) and measure the models against that.
 
# ## 7. Handling class imbalance
# 
# Three common options, tested here on Logistic Regression so the comparison stays fair:
# 
# * **No handling**: the baseline
# * **Class weights**: errors on small classes cost more
# * **SMOTE**: creates synthetic training samples for the small classes
# 
# (Focal Loss is mainly used when training neural networks, so it belongs in the deep-learning stage.)
 
# In[14]:
 
 
def evaluate_lr(X_fit, y_fit, class_weight=None):
    """Train a Logistic Regression and return its test-set scores."""
    model = LogisticRegression(max_iter=1000, class_weight=class_weight)
    model.fit(X_fit, y_fit)
    y_pred = model.predict(X_test)
    return {
        "macro_f1": f1_score(y_test, y_pred, average="macro"),
        "negative_recall": recall_score(y_test, y_pred, labels=[0], average=None)[0],
        "accuracy": accuracy_score(y_test, y_pred),
    }
 
 
X_smote, y_smote = SMOTE(random_state=RANDOM_STATE).fit_resample(X_train, y_train)
 
imbalance_results = pd.DataFrame({
    "No handling": evaluate_lr(X_train, y_train),
    "Class weights": evaluate_lr(X_train, y_train, class_weight="balanced"),
    "SMOTE": evaluate_lr(X_smote, y_smote),
}).T.round(3)
 
display(imbalance_results)
 
 
# Look at `negative_recall` (what share of truly negative posts the model finds). A strategy that raises it
# without hurting macro F1 too much is the better choice for risk monitoring.
 
# ## 8. Explainable AI
# 
# Investors need to know **why** a post was called bullish or bearish. We use two views:
# 
# 1. **Logistic Regression coefficients:** which words push a post toward each sentiment
# 2. **SHAP values:** how much each feature moved each individual prediction
 
# In[15]:
 
 
lr_model = fitted_models["Logistic Regression"]
coef = pd.DataFrame(lr_model.coef_.T, index=feature_names, columns=class_names)
word_coef = coef.loc[list(tfidf.get_feature_names_out())]          # words only (skip numeric features)
 
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
for ax, sentiment, color in zip(axes, ["negative", "positive"], ["#d1495b", "#2a9d8f"]):
    top = word_coef[sentiment].sort_values(ascending=False).head(12)[::-1]
    ax.barh(top.index, top.values, color=color)
    ax.set_title(f"Words pushing a post toward '{sentiment}'")
    ax.set_xlabel("Coefficient")
save_and_show("04_top_words_by_sentiment")
 
 
# In[16]:
 
 
# SHAP on the Logistic Regression model (linear explainer is fast and exact for linear models)
rng = np.random.RandomState(RANDOM_STATE)
background = X_train[rng.choice(X_train.shape[0], 100, replace=False)].toarray()
sample = X_test[rng.choice(X_test.shape[0], min(300, X_test.shape[0]), replace=False)].toarray()
 
explainer = shap.LinearExplainer(lr_model, background)
shap_values = explainer.shap_values(sample)
 
# Different shap versions return a list (one array per class) or one 3D array; make it (samples, features, classes)
shap_array = np.stack(shap_values, axis=-1) if isinstance(shap_values, list) else shap_values
 
importance = pd.DataFrame(np.abs(shap_array).mean(axis=0), index=feature_names, columns=class_names)
importance["overall"] = importance.mean(axis=1)
 
top_features = importance["overall"].sort_values(ascending=False).head(15)[::-1]
plt.figure(figsize=(8, 5))
plt.barh(top_features.index, top_features.values, color="#457b9d")
plt.title("Top 15 features by average |SHAP| (all classes)")
plt.xlabel("Mean absolute SHAP value")
save_and_show("05_shap_importance")
 
 
# ## 9. Real Estate Sentiment Index (RESI), trend and early warning
# 
# Investors understand an **index** better than a label. RESI converts monthly sentiment into one number from 0 to 100:
# 
# $$\text{RESI} = 50 + 50 \times \frac{\text{positive} - \text{negative}}{\text{positive} + \text{negative} + k}$$
# 
# * We ignore neutral posts, because they carry no opinion (and make up most of the data).
# * `k` is a small smoothing constant that stops months with very few opinionated posts from jumping to extreme values.
# * 50 means balanced. Above 50 is bullish and below 50 is bearish.
# 
# | RESI | Meaning |
# |---|---|
# | 70 and above | Strong Bullish |
# | 55 to 70 | Bullish |
# | 45 to 55 | Neutral |
# | 30 to 45 | Bearish |
# | below 30 | Strong Bearish |
 
# In[17]:
 
 
df["month"] = df["published_at"].dt.to_period("M")
 
recent = df[df["published_at"] >= TIME_SERIES_START]     # older posts are too sparse for a monthly index
 
monthly = (
    recent.groupby("month")
      .agg(posts=("id", "size"),
           positive=("sentiment_label", lambda s: (s == "positive").sum()),
           negative=("sentiment_label", lambda s: (s == "negative").sum()))
)
monthly = monthly[monthly["posts"] >= MIN_POSTS_PER_MONTH].copy()   # drop months that are too small to trust
 
 
def resi_band(value):
    if value >= 70: return "Strong Bullish"
    if value >= 55: return "Bullish"
    if value >= 45: return "Neutral"
    if value >= 30: return "Bearish"
    return "Strong Bearish"
 
 
monthly["resi"] = 50 + 50 * (monthly["positive"] - monthly["negative"]) / (
    monthly["positive"] + monthly["negative"] + RESI_SMOOTHING)
monthly["resi_3m_avg"] = monthly["resi"].rolling(3, min_periods=1).mean()   # smooths month-to-month noise
monthly["band"] = monthly["resi"].apply(resi_band)
 
# trend: compare the 3-month average with the previous month's value
change = monthly["resi_3m_avg"].diff()
monthly["trend"] = np.select([change > 2, change < -2], ["Rising confidence", "Falling confidence"], default="Stable")
 
# early warning: a drop or rise of 10+ points compared with two months ago
two_month_change = monthly["resi_3m_avg"].diff(2)
monthly["alert"] = np.select(
    [two_month_change <= -10, two_month_change >= 10],
    ["SENTIMENT DROP", "RECOVERY SIGNAL"], default="")
 
print(f"Index covers {monthly.index.min()} to {monthly.index.max()} ({len(monthly)} months, {len(recent):,} posts)")
display(monthly[["posts", "positive", "negative", "resi", "resi_3m_avg", "band", "trend", "alert"]].round(1))
 
 
# In[18]:
 
 
fig, ax = plt.subplots(figsize=(12, 5))
x = monthly.index.astype(str)
 
# background bands
for low, high, color in [(70, 100, "#2a9d8f"), (55, 70, "#a8dadc"), (45, 55, "#e9ecef"), (30, 45, "#f4a261"), (0, 30, "#d1495b")]:
    ax.axhspan(low, high, color=color, alpha=0.18)
 
ax.plot(x, monthly["resi"], marker="o", color="#457b9d", label="RESI (monthly)")
ax.plot(x, monthly["resi_3m_avg"], color="#1d3557", linewidth=2.5, label="3-month average")
 
# mark alerts
for position, (month, row) in enumerate(monthly.iterrows()):
    if row["alert"]:
        ax.annotate(row["alert"], (position, row["resi"]), textcoords="offset points", xytext=(0, 14),
                    ha="center", fontsize=8, color="#d1495b" if "DROP" in row["alert"] else "#2a9d8f",
                    arrowprops=dict(arrowstyle="-", color="gray"))
 
ax.set_ylim(20, 100)
ax.set_title("Real Estate Sentiment Index (RESI)")
ax.set_ylabel("Index (0-100)")
ax.legend(loc="upper left")
plt.xticks(rotation=45, ha="right")
save_and_show("06_resi_trend")
 
 
# ## 10. Market risk traffic light
# 
# The dataset has no "risk" label, so we build a transparent **rule-based risk score** instead of pretending to predict one.
# Each post gets one risk point for each of these signals:
# 
# * negative sentiment
# * crisis signal
# * bearish financial signal
# 
# (The dataset also has an `is_fud` flag, but it is empty for every real-estate post, so we leave it out.)
# Crisis and bearish signals are rare, so the score is dominated by negative sentiment. That is fine for a first version,
# but it is one more reason to add richer risk data later.
# 
# A month's risk score is the average points per post. We then compare it with the project's own history:
# **Green** = lowest third, **Yellow** = middle third, **Red** = highest third.
 
# In[19]:
 
 
df["risk_points"] = (
    (df["sentiment_label"] == "negative").astype(int)
    + df["crisis_signal"].astype(int)
    + (df["financial_signal"] == "bearish").astype(int)
)
 
monthly["risk_score"] = recent_risk = df[df["published_at"] >= TIME_SERIES_START].groupby("month")["risk_points"].mean().reindex(monthly.index)
 
low_cut, high_cut = monthly["risk_score"].quantile([0.33, 0.67])
monthly["risk_level"] = np.select(
    [monthly["risk_score"] <= low_cut, monthly["risk_score"] >= high_cut],
    ["Green", "Red"], default="Yellow")
 
print("Share of posts carrying each risk signal:")
print("crisis:", round(df["crisis_signal"].mean(), 3), "| bearish:", round((df["financial_signal"] == "bearish").mean(), 3))
display(monthly[["posts", "risk_score", "risk_level"]].round(3))
 
 
# ## 11. Investor dashboard
 
# In[20]:
 
 
latest = monthly.iloc[-1]
latest_month = str(monthly.index[-1])
 
fig, axes = plt.subplots(2, 2, figsize=(15, 9))
fig.suptitle(f"US Real Estate Market Intelligence: latest month {latest_month}", fontsize=15, fontweight="bold")
 
# 1) market mood gauge (a simple horizontal gauge)
ax = axes[0, 0]
for low, high, color in [(0, 30, "#d1495b"), (30, 45, "#f4a261"), (45, 55, "#e9ecef"), (55, 70, "#a8dadc"), (70, 100, "#2a9d8f")]:
    ax.barh(0, high - low, left=low, color=color, height=0.5)
ax.axvline(latest["resi"], color="black", linewidth=3)
ax.set_xlim(0, 100)
ax.set_yticks([])
ax.set_title(f"Market mood: RESI {latest['resi']:.0f} ({latest['band']})")
ax.set_xlabel("0 = Strong Bearish   |   50 = Neutral   |   100 = Strong Bullish")
 
# 2) sentiment trend
ax = axes[0, 1]
ax.plot(monthly.index.astype(str), monthly["resi"], marker="o", color="#457b9d", label="RESI")
ax.plot(monthly.index.astype(str), monthly["resi_3m_avg"], color="#1d3557", linewidth=2.5, label="3-month avg")
ax.axhline(50, color="gray", linestyle="--", linewidth=1)
ax.set_title("Sentiment trend")
ax.tick_params(axis="x", rotation=60)
ax.legend()
 
# 3) most discussed topics
ax = axes[1, 0]
topic_counts = topic_summary["posts"].sort_values()
ax.barh(topic_counts.index, topic_counts.values, color="#457b9d")
ax.set_title("Most discussed topics")
ax.set_xlabel("Posts")
 
# 4) risk traffic light by month
ax = axes[1, 1]
light_colors = monthly["risk_level"].map({"Green": "#2a9d8f", "Yellow": "#e9c46a", "Red": "#d1495b"})
ax.bar(monthly.index.astype(str), monthly["risk_score"], color=light_colors)
ax.set_title("Risk traffic light (rule-based)")
ax.set_ylabel("Risk score")
ax.tick_params(axis="x", rotation=60)
 
save_and_show("07_investor_dashboard")
 
 
# ## 12. Save outputs and create a reusable prediction function
# 
# We save the trained pieces (TF-IDF, scaler, model, label encoder) so a web API can load them later.
# The `predict_sentiment()` function below is exactly what a FastAPI endpoint (`POST /predict-sentiment`) would call.
 
# In[21]:
 
 
# Save tables
monthly.reset_index().astype({"month": str}).to_csv(os.path.join(OUTPUT_DIR, "monthly_resi.csv"), index=False)
df[["id", "platform", "published_at", "content", "clean_text", "sentiment_label", "topic", "risk_points"]].to_csv(
    os.path.join(OUTPUT_DIR, "clean_real_estate_posts.csv"), index=False)
 
# Save the best model and all preprocessing objects together
joblib.dump({"model": best_model, "tfidf": tfidf, "scaler": scaler, "label_encoder": label_encoder,
             "model_name": best_name}, os.path.join(OUTPUT_DIR, "sentiment_model.joblib"))
 
 
def predict_sentiment(text):
    """Predict bullish / neutral / bearish for one post, with class probabilities when the model supports them."""
    bundle = joblib.load(os.path.join(OUTPUT_DIR, "sentiment_model.joblib"))
    features = bundle["scaler"].transform(extract_features([text]))
    text_matrix = bundle["tfidf"].transform([clean_text(text)])
    X_new = hstack([text_matrix, csr_matrix(features)]).tocsr()
 
    predicted = bundle["label_encoder"].inverse_transform(bundle["model"].predict(X_new))[0]
    result = {"sentiment": predicted, "market_view": {"positive": "Bullish", "neutral": "Neutral", "negative": "Bearish"}[predicted]}
    if hasattr(bundle["model"], "predict_proba"):
        probabilities = bundle["model"].predict_proba(X_new)[0]
        result["probabilities"] = dict(zip(bundle["label_encoder"].classes_.tolist(), probabilities.astype(float).round(3).tolist()))
    return result
 
 
examples = [
    "Housing demand is strong and home prices keep rising in growing metro areas. Great time to invest!",
    "Mortgage rates are crushing buyers. Inventory is falling and a market crash feels likely.",
    "The city council will discuss the new zoning proposal on Tuesday.",
]
for text in examples:
    print(text[:75], "->", predict_sentiment(text))
 
print("\nSaved files:", sorted(os.listdir(OUTPUT_DIR)))