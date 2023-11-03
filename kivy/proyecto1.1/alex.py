from matplotlib import pyplot as plt
l1=[]
l2=[]
for i in range(0,20):
    i=i-5
    l1.append(i)
    i1=5*i-i*i
    l2.append(i1)
plt.plot(l1,l2)
plt.show()