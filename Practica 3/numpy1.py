import numpy as np

a = np.array([10, 10, 329, 128, 10])
b = np.full((3, 5, 4), 7)
c = np.random.random((3, 5, 4))
d = np.nan
np.savetxt("dataOne.csv", a)
e = np.loadtxt("dataOne.csv", delimiter=';')
print(c)
print(e)