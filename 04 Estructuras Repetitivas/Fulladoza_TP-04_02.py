nro = int(input("Ingrese un número entero: "))
c = 0
while nro > 0:
    c+=1
    nro//=10
print(c)