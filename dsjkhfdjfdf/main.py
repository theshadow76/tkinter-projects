from math import *
def premier(n):
    reponse = True
    r = int(sqrt(n))
    for p in range(2, r + 1):
        if n%p == 0:
            reponse = False
    print(reponse)
    return reponse
premier(65)