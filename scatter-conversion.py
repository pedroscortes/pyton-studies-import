import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("leads-conversion.csv")
x = dataframe.count_won
y = dataframe.count_lost
plt.scatter(x, y)
plt.show()