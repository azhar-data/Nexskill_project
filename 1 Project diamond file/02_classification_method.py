import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
 
# 1. Load the data
df = pd.read_csv("1 project diamond file/10-diamonds.csv")
df = df.drop(columns=df.columns[0])      # first column is just a row number
 
# 2. Turn text columns into numbers (models only understand numbers)
for col in ["color", "clarity"]:
    df[col] = LabelEncoder().fit_transform(df[col])
 
# 3. Split into inputs (X) and the thing we want to predict (y)
X = df.drop(columns=["cut"])
y = df["cut"]
 
# 4. Split into training data (80%) and test data (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
 
# 5. Train two models
tree = DecisionTreeClassifier(max_depth=10, random_state=42)
forest = RandomForestClassifier(n_estimators=100, random_state=42)
tree.fit(X_train, y_train)
forest.fit(X_train, y_train)
 
# 6. Check how well each one does on data it has never seen
print("Decision Tree accuracy :", round(accuracy_score(y_test, tree.predict(X_test)), 3))
print("Random Forest accuracy :", round(accuracy_score(y_test, forest.predict(X_test)), 3))
 
# 7. Detailed results for the Random Forest
pred = forest.predict(X_test)
print("\nDetailed report:\n", classification_report(y_test, pred))
print("Confusion matrix:\n", confusion_matrix(y_test, pred))
 
# 8. Which columns mattered most?
importance = pd.Series(forest.feature_importances_, index=X.columns)
print("\nMost important columns:\n", importance.sort_values(ascending=False).round(3))