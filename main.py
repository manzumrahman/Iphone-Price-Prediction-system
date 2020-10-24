import pandas
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plotter

data = pandas.read_csv("iphone_price.csv")
model = LinearRegression()
model.fit(data[["version"]], data[["price"]])
plotter.bar(data["version"], data['price'])
version = int(input("Price of which version do you want to know?"))
print("Price = ", model.predict([[version]])[0][0], "approximately")
plotter.show()
