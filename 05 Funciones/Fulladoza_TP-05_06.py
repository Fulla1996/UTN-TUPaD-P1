def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

nro = int(input("Ingrese un número entero: "))
tabla_multiplicar(nro)