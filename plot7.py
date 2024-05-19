import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

student =np.array(["Harshit","Sarthak","Pragyan","Ankush"])
marks=np.array([90,95,80,75])

plt.pie(marks,labels=student,autopct='%1.2f%%')

plt.show()
