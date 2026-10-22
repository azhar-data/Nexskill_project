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

sns.histplot(data=df,x='lunch',y='reading score')
plt.show()
sns.histplot(data=df,x='lunch',y='writing score')
plt.show()
sns.catplot(data=df,x='lunch',y='math score')
plt.show()
sclaer=StandardScaler()
X=sclaer.fit_transform(df[['reading score','writing score','math score']])

y=df['lunch_encoded']
print(X)
print(y)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,
                                                y,
                                                train_size=.8,
                                                random_state=45
                                                )

print(X_test)
print(X_train)
print(y_test)
print(y_train)

#svm model are used
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Classification model
model = RandomForestClassifier(n_estimators=300, max_depth=10, random_state=45)

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

