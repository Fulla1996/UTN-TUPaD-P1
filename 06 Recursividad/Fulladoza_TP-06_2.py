def fibonacci(nro):
    if nro == 0 or nro == 1:
        return nro
    return fibonacci(nro-1) + fibonacci(nro-2)

nroObjetivo = -1
print("Bienvenido a la calculadora consecutiva de la serie fibonacci!")

while nroObjetivo <= 0:
    nroObjetivo = int(input("Ingrese el número positivo hasta el que desea calcular: "))

for i in range(2, nroObjetivo):
    print(f"Fibonacci en posición {i} = {fibonacci(i)}")