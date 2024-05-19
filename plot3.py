import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data={
    "Cars":["BMW","MERCEDES","AUDI","BENTELY"],
    "Price(IN THOUSANDS)":[10000,50000,80000,90000],
    "Year of launch":[2012,2013,2017,2019]
}
dataframe=pd.DataFrame(data)
plt.plot(dataframe["Price(IN THOUSANDS)"],dataframe["Year of launch"])
plt.grid()
plt.show()