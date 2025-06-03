def operaciones_basicas(a, b):
    if b != 0:
        tupla = (a+b,a-b,a*b,a/b)
    else:
        tupla = (a+b,a-b,a*b,"No se puede dividir por 0")
    return tupla

nro1 = int(input("Ingrese el primer número: "))
nro2 = int(input("Ingrese el segundo número: "))

tupla_resultado = operaciones_basicas(nro1, nro2)
print(f"{nro1} + {nro2} = {tupla_resultado[0]}")
print(f"{nro1} - {nro2} = {tupla_resultado[1]}")
print(f"{nro1} * {nro2} = {tupla_resultado[2]}")
print(f"{nro1} / {nro2} = {tupla_resultado[3]}")