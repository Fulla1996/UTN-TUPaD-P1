contactos = {}

print("Bienvendio a su Agenda")
print("Por favor cargue 5 contactos: ")

for i in range (5):
    nombre = input("Ingrese el nombre: ").lower()
    tel = input("Ingrese su ´numero de teléfono: ")
    contactos[nombre] = tel

while True:
    nombre = input("Ingrese un nombre para consultar en la Agenda o Salir para abandonar la agenda: ").lower()
    if nombre == "salir":
        break
    if nombre in contactos:
        print(contactos[nombre])
    else:
        print(f"{nombre.capitalize()} no existe en Contactos")
