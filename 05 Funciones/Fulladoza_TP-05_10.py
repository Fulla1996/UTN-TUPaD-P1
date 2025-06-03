def calcular_promedio(a, b,c):
    return (a+b+c)/3

nro1 = int(input("Ingrese el primer número: "))
nro2 = int(input("Ingrese el segundo número: "))
nro3 = int(input("Ingrese el tercer número: "))

print(f"El promedio de {nro1}, {nro2} y {nro3} es {calcular_promedio(nro1,nro2,nro3)}")
