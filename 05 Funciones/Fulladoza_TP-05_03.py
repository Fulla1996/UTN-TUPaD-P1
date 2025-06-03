def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellido: ")
eda = input("Ingrese su edad: ")
res = input("Ingrese su residencia: ")

informacion_personal(nom, ape, eda, res)