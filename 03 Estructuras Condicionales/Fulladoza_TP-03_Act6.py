import random as r
from statistics import mode, median, mean

numeros_aleatorios = [r.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(numeros_aleatorios)

print(f"La moda es {moda}")
print(f"La mediana es {mediana}")
print(f"La media es {media}")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")