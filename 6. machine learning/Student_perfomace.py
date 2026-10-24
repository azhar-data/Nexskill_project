import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
df=pd.read_csv('6. machine learning/StudentsPerformance.csv')
print(df)

print(df.describe())
print(df.dtypes)
print(df.info())
print(df.describe())
df = df.dropna()
df=df.drop_duplicates()
print(df.isnull().sum())



from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['lunch_encoded']=le.fit_transform(df['lunch'])
df['test preparation course']=le.fit_transform(df['test preparation course'])
sns.lineplot(data=df,x='test preparation course',y='lunch')
plt.show()
sclaer=StandardScaler()
X=df[['math score', 'reading score', 'writing score']]

y=df['test preparation course']
print(X)
print(y)

from sklearn.model_selection import train_test_split,cross_val_score

X_train,X_test,y_train,y_test=train_test_split(X,
                                                y,
                                                train_size=.7,
                                                random_state=42
                                                )

print(X_test)
print(X_train)
print(y_test)
print(y_train)

X_test=sclaer.fit_transform(X_test)
X_train=sclaer.fit_transform(X_train)
#svm model are used
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Classification model
model = LogisticRegression(),RandomForestClassifier()


model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)



# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

