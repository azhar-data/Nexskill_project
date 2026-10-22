import pandas as pd 
from sklearn.datasets import load_digits

load_data=load_digits()

load_data_reterun_x_y=load_digits(return_X_y=True)

print(load_data_reterun_x_y)
print(load_data_reterun_x_y[0])
print(load_data_reterun_x_y[1])
print()
print(load_data)

load_data_as_frame=load_digits(as_frame=True)
print('load data as frame :',load_data_as_frame)

load_df=pd.DataFrame(load_data.data,columns=load_data.feature_names)
print('load digits are as :',load_df)
print()
load_df['target']=load_data.target

print('header of the file',load_df.head())
print('info of the file are as :',load_df.info())
print('type of the file :',load_df.dtypes)
print('decribe of the file are as:',load_df.describe())
print('tail of the file arre as :',load_df.tail())

from sklearn.preprocessing import StandardScaler
X=load_df[load_data.feature_names].copy()
y=load_df['target'].copy()
print('X:',X)
print('y:',y)



sclaer=StandardScaler()
sclaer.fit(X)
X_scaled=sclaer.transform(X.values)

print(X_scaled[0])

from sklearn.model_selection import train_test_split

X_train_scaled,X_test_scaled,y_train,y_test=train_test_split(X_scaled,
                                                                             y,
                                                                         train_size=.4,
                                                                         random_state=25)


print(f'train size: {round(len(X_train_scaled) / len(X) * 100)}% \n\
Test size: {round(len(X_test_scaled) / len(X) * 100)}%')

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
#train of the model
logistic_regression=LogisticRegression()
svm=SVC()
tree=DecisionTreeClassifier()
logistic_regression.fit(X_train_scaled,y_train)
svm.fit(X_train_scaled,y_train)
tree.fit(X_train_scaled,y_train)

#preduction of the model 
log_reg_pred=logistic_regression.predict(X_test_scaled)
svm_pred=svm.predict(X_test_scaled)
tree_pred=tree.predict(X_test_scaled)

from sklearn.metrics import classification_report


model_preds={
    'logistic regression':log_reg_pred,
    'support vactor machine':svm_pred,
    'decsion tree':tree_pred
}
for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(y_test, preds)}", sep="\n\n")

