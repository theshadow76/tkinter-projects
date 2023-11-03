registrarse_nombre = None
registrarse_edad = None
registrarse_email = None
data = None

print("\t bienvenido al Login mas malo del mundo!")
print("para empezar puedes decidir de registrarte o logeaerte")
print("1. registrarse")
print("2. login")

v1 = input("diga que quiere hacer: ")

def registrarse():
    print("\t Ok! a registrarse")
    registrarse_nombre = input("cual es tu nombre: ")
    registrarse_edad = input("digite su edad: ")
    registrarse_email = input("digite su email: ")

    print("ok! ", registrarse_nombre, " tu edad es de ", registrarse_edad, " y su email es ", registrarse_email)

    print("ahora te vamos a agregar a nuestra bases de datos")
    data = open("data.txt", "a")
    data.write(registrarse_nombre)
    data.write("\n")
    data.write(registrarse_edad)
    data.write("\n")
    data.write(registrarse_email)
    data.write("\n")
    data.close()

if (v1 == "1"):
    registrarse()
else:
    print("error, not posible that number")