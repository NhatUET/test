from pandas import read_csv
import numpy as np
import sklearn.impute as ski
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
dataset = read_csv('D:\Code Assignment\Python3\data\data.csv')
X = dataset.iloc[:3, :-1].values
imputer = ski.SimpleImputer(missing_values=np.nan, strategy='mean')

imputer.fit(X[:,1:3])

X[:,1:3] = imputer.transform(X[:,1:3])
print(X)


ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])] , remainder="passthrough" )
X = np.array(ct.fit_transform(X))
print(X)
print('-----------------\n')
le = LabelEncoder()
#output of fit_transform of Label Encoder is already a Numpy Array
y = le.fit_transform(X)
#y = [0 1 0 0 1 1 0 1 0 1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
print(X_train.shape)