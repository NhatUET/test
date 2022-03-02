# summarize the number of unique values for each column using numpy
# from re import T
# from numpy import loadtxt
# from numpy import unique
# # load the dataset
# data = loadtxt('D:\Code Assignment\Python3\data\oil_spill.csv', delimiter=',')
# # summarize the number of unique values in each column
# for i in range(data.shape[1]):
# #    print(i, len(unique(data[:, i])))
#     num = len(unique(data[:, i]))
#     percentage = float(num) / data.shape[0] * 100
#     if percentage < 1:
#         print('%d, %d, %.1f%%' % (i, num, percentage))





# using pandas  
from asyncio import threads
from numpy import arange
from pandas import read_csv
from sklearn.feature_selection import VarianceThreshold
from matplotlib import pyplot

#load data
df = read_csv('D:\Code Assignment\Python3\data\oil_spill.csv', header=None)
data = df.values
X = data[:, :-1]
y = data[:,-1]
print(X.shape, y.shape)
# # define the transform
# transform = VarianceThreshold()
# # transform the input data
# X_sel = transform.fit_transform(X)
# print(X_sel.shape)

thresholds = arange(0.0, 0.55, 0.05)

results = list()

for t in thresholds:
    transform = VarianceThreshold(threshold=t)
    X_sel = transform.fit_transform(X)

    n_features = X_sel.shape[1]
    print('>Threshold=%.2f, Features = %d' % (t, n_features))

    results.append(n_features)

pyplot.plot(thresholds,results)
pyplot.show()

print(df.shape) 
counts = df.nunique() 
to_del = [i for i, v in enumerate(counts) if float(v)/df.shape[0] * 100 < 1]  
print(to_del)
df.drop(to_del, axis=1, inplace=True)
print(df.shape)



