def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n-1)

print(contar_bloques(1))