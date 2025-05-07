nro = int(input("Ingrese un número para ser invertido: "))
nroFin = 0
while nro > 0:
    nroFin += nro%10
    nro//=10
    if nro > 0:
        nroFin*=10

print(nroFin)