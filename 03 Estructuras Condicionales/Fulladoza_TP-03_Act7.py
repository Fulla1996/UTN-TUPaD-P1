frase = input("Ingrese una frase: ")
if frase[-1].lower() in ("a","e","i", "o", "u"):
    frase = frase + "!"
print(frase);