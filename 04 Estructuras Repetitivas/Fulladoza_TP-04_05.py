import random

nroSecreto = random.randint(0,9)
c = 1

nro = int(input("Intente adivinar el número secreto (0 - 9): "))

while nro != nroSecreto:
    nro = int(input("Intente nuevamente: "))
    c+=1

print(f"Lo logro en tan solo {c} intentos!")