"""
Modules:
pandas
sklearn

Pandas to bring csv file into python file
A CSV is a comma-separated values file, which allows data to be saved in a tabular format.
You can use a CSV file to move data between programs that aren't ordinarily able to exchange data.
sklearn for linear regression{To predict the price of the model}
LinearRegression(): run the model
model.fit : To fit the model by feeding data
Here:
Predicting the version of 14 and 30
"""

import pandas
from sklearn.linear_model import LinearRegression
data=pandas.read_csv('iphone_price.csv')

model=LinearRegression()
model.fit(data[['version']],data[['price']])
print(model.predict([[14]]))
print(model.predict([[30]]))