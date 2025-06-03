def factorial(nro):
    if nro == 1:
        return 1
    
    return nro * factorial(nro-1)

nroObjetivo = -1
print("Bienvenido a la calculadora consecutiva de factoriales!")
while nroObjetivo <= 0:
    nroObjetivo = int(input("Ingrese el número positivo hasta el que desea calcular: "))

for i in range(2, nroObjetivo ):
    print(f"{i}! = {factorial(i)}")