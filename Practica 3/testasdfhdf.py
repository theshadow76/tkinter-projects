l1=[x for x in range(1000)]
l2=[100-x for x in range(1000)]
import matplotlib.pyplot as plt
plt.plot(l1,l2)
plt.show()