from pandas import read_csv
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
from numpy import percentile
seed(1)
data = 5 * randn(10000) + 50

q25, q75 = percentile(data, 25), percentile(data, 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))

cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
outliers = [x for  x in data if x < lower or x > upper] 
print('Indentified outliers: %d' % len(outliers))

outliers_removed = [x for x in data if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))



# print('mean=%.3f stdv=%.3f' % (mean(data), std(data)))

# data_mean, data_std = mean(data), std(data)

# cut_off = data_std * 3
# lower, upper = data_mean - cut_off, data_mean + cut_off

# outliers = [x for  x in data if x < lower or x > upper] 
# print('Indentified outliers: %d' % len(outliers))

# outliers_removed = [x for x in data if x >= lower and x <= upper]
# print('Non-outlier observations: %d' % len(outliers_removed))

# df = read_csv('D:\Code Assignment\Python3\data\iris.csv', header=None)
# dups = df.duplicated()
# print(dups.any())
# print(df[dups])
# print(df.shape) 
# df.drop_duplicates(inplace = True)
# print(df.shape)

