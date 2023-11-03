import numpy as np
import matplotlib.pyplot as plt

T = np.array([1, 2, 3])
U = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
I = np.array([0, 0.95e-3, 2.02e-3, 3.05e-3, 3.96e-3, 5.02e-3, 5.94e-3, 6.99e-3,8.02e-3, 9.04e-3])
R = U / I
P = U * I
R = 1005

print(f'{U[2]} && {I[2]} La 3 ieme valeur de la tension est: {U[2]} V')

print(f'{R}  {P}')
U = np.append(U, 20)
I = np.append(I, 19.9e-3)
Umod = R * I

plt.plot(I,U, "b+")
plt.plot(I,Umod, "rx-")
plt.legend()
plt.title('ShadowTask is really cool')
plt.xlabel('AXE X')
plt.grid(True)
plt.show()

T = np.append(T, 8)
