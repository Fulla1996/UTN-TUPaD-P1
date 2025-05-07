sum = 0

while True:
    nro = int(input("Ingrese un número o 0 para salir: "))
    if nro == 0:
        break
    else:
        sum += nro

print(f"La suma de todos los números ingresados es {sum}")