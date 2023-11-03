import numpy as np

a = np.array([12, 3, 233, 543, 4, 34])

b = np.savetxt("gay.csv", a)
c = np.loadtxt("gay.csv", delimiter=";")
print(c)