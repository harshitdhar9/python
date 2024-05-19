import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

student =[1,2,3,4,5]
marks=[90,95,80,75,3]
range=[5,10,15,20,25]

plt.scatter(student,range,color='r')
plt.scatter(marks,range,color='b')

plt.show()
