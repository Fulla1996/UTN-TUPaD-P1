def es_palindromo(palabra):
    if len(palabra)<=1:
        return True
    
    if (palabra[0] != palabra[-1]):
        return False
    
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese palabra a comprobar: ").lower()

if es_palindromo(palabra):
    print(f"La palabra \"{palabra}\" es un palíndromo")
else:
    print(f"La palabra \"{palabra}\" no es un palindromo")