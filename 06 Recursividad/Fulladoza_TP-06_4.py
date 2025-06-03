def decimal_a_binario(dec):
    if dec == 0 or dec == 1:
        return str(dec)
    return str(decimal_a_binario(dec//2)) + str(dec%2)

nroDec = -1
print("Bienvenido al conversor Decimal a Binario!")

while nroDec <= 0:
    nroDec = int(input("Ingrese el número entero positivo a convertir: "))

print(f"El número {nroDec} en Binario es: {decimal_a_binario(nroDec)}")