nombre = input("Ingrese su nombre: ")


while True:
    op = int(input("Ingrese la opción deseada\n\t1 - Mayúsculas\n\t2 - Minúsculas\n\t3 - Primera letra en mayúsculas\n\nOpción: "))
    match op:
        case 1:
            print(nombre.upper())
            break
        case 2:
            print(nombre.lower())
            break
        case 3:
            print(nombre.title())
            break
        case _:
            print("Opción no válida")
            