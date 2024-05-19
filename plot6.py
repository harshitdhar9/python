import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

student =np.array(["David","Kirti","Abhay","Prakash"])
marks=np.array([90,95,80,75])

plt.bar(student,marks)
plt.xlabel("students")
plt.ylabel("marks")
plt.title("Student marks")
plt.show()