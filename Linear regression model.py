# import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# import dataset
dataset = pd.read_csv('Student data.csv')
X = dataset.iloc[:, 0:1].values # independent var study hours
y = dataset.iloc[:, 1:].values  # dependent var student scores

# data splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model training
regressor= LinearRegression()
regressor.fit(X_train, y_train)

regressor

# model testing
y_pred = regressor.predict(X_test)

print(regressor.coef_,
regressor.intercept_)


# Visualising training data
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Training data')
plt.xlabel('Study hours')
plt.ylabel('Score')
plt.show()

# Visualising testing data
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Training data')
plt.xlabel('Study hours')
plt.ylabel('Score')
plt.show()

