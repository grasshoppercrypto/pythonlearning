import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline

data = pd.read_csv('/Users/yifanhuang/Downloads/ML_1/python_code/data/Advertising.csv',index_col=0)
print(data.head())
print(data.shape)
print(data.describe())

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111)
ax.boxplot([data.TV, data.radio, data.newspaper, data.sales], labels=['TV','Radio','Newspaper','Sales'])
#plt.show()

fig, axs = plt.subplots(1, 3, sharey = True)
data.plot(kind='scatter', x='TV', y='sales', ax=axs[0], figsize=(16,8))
data.plot(kind='scatter', x='radio', y='sales', ax=axs[1])
data.plot(kind='scatter', x='newspaper', y='sales', ax=axs[2])
plt.show()
