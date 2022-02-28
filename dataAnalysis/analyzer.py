from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import statsmodels.api as sm

ytData = pd.read_csv('../webscraper/dataByYear.csv')

X = sm.add_constant(ytData['Year'])
model = sm.OLS(ytData['Annual_Views'], X).fit()
pred1 = model.predict(X)

print_model = model.summary()
print(print_model)

ax = ytData.plot()
ax.xaxis.set_ticks(ytData.index)
ax.xaxis.set_ticklabels(ytData['Year'])
ax.ticklabel_format(style='plain',axis='y')
plt.xticks(rotation=45)
plt.yticks(range(0,6600000, 500000))
plt.show()

plt.scatter(ytData['Year'], ytData['Annual_Views'])
plt.xticks(rotation=45)
plt.yticks(range(0,6600000, 500000))
plt.show()

years = []

x_train, x_test, y_train, y_test = train_test_split(ytData.Year, ytData.Annual_Views, test_size=0.8)
regr = LinearRegression()
regr.fit(np.array(x_train).reshape(-1,1),y_train)

predictions = regr.predict(np.array(x_test).reshape(-1,1))
print(y_test.head())
print(predictions)

residuals = predictions - y_test
print(residuals)
plt.hist(residuals)
plt.show()

fig, ax1 = plt.subplots(1,1,figsize=(10,7),tight_layout=True)
ax1.hist(residuals)
ax1.ticklabel_format(style='plain',axis='x')
plt.show()

print(mean_squared_error(y_test, predictions) ** 0.5)
