import random

autos = ['1', '2', '3', '4', '5']

a = random.choice(autos)

b = input("diga su numero: ")

correct = a

while (b == correct):
    print("correcto")
    break
while (b != correct):
    print("Incorrecto")
    break
print(a)

