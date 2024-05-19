import matplotlib.pyplot as plt
import numpy as np
a=np.arange(5)
b=[2,3,4,5,6]
c=[1,3,4,5,7]
fig=plt.figure()
ax=plt.subplot()
ax.plot(a,b,"k--",label="Frequency")
ax.plot(a,c,"k:",label="Periods")
ax.legend() #loc as parameter and fontsize
plt.grid()
plt.title(label="Frequency of signal")
plt.show()
