def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero==digito else 0
    return (1 if numero%10==digito else 0) + contar_digito(numero//10, digito)

print(contar_digito(123456,7))