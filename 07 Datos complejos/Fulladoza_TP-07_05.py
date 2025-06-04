frase = input("Ingrese una frase: ")

palabras_unicas = set(frase.split())
recuento_palabras = {}

for palabra in palabras_unicas:
    recuento_palabras[palabra] = frase.count(palabra)

print(f"Palabras_únicas: {palabras_unicas}")
print(f"Recuento: {recuento_palabras}")