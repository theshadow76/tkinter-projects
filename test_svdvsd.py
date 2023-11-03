import random

numeros = ['1', '2', '3', '4', '5']

a = random.choice(numeros)

print("diga un numero entre los numeros 1 a 5")

inp1 = input("aqui: ")

correct = a

while (inp1 == correct):
    print("correcto!")
    break
while (inp1 != correct):
    print("incorrecto")
    break

print(a)

