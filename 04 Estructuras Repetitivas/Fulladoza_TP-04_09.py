CANTIDAD_VALORES = 100 #Variable para cantidad de valores a ingresar
sum = 0

for i in range(CANTIDAD_VALORES):
    nro = int(input(f"Ingrese el {i+1}° número entero: "))
    sum+=nro

print(f"El promedio es {sum / CANTIDAD_VALORES}")