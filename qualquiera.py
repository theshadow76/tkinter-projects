import random as r
l1='abcdefghijklmnopqrstuvwxyz0123456789'
l1=list(l1)
l2=str()
for s in range(8):
    v1=r.choice(l1)
    l2=l2+v1
print(l2)