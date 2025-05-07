cPar = 0
cImpar = 0
cNeg = 0
cPos = 0

for i in range(100):
    nro = int(input(f"Ingrese el {i+1}° numero: "))
    if nro%2 == 1:
        cImpar+=1
    else:
        cPar+=1
    if nro > 0:
        cPos+=1
    if nro < 0:
        cNeg+=1

print(f"Se ingresaron:\n\t {cPar} números pares\n\t {cImpar} números impares\n\t {cPos} números positivos\n\t {cNeg} números negativos")