while True:
    hemisferio = input("Ingrese cual es su hemisferio (N o S): ")
    if (hemisferio[0].upper() not in ("N", "S")):
        print("Ingrese una opción correcta.")
    else:
        break

while True:
    mes = int(input("Ingrese el mes en números (1 a 12): "))
    if (mes < 1 or mes > 12):
        print("Ingrese un mes válido")
    else:
        break

while True:
    dia = int(input("Ingrese el día: "))
    if (dia > 31):
        print("Ingrese un número correcto")
    elif (dia > 30 and mes in (4,6,9,11)):
        print("Ingrese un número correcto")
    elif (dia > 29 and mes == 2):
        print("Ingrese un número correcto")
    else:
        break

if (hemisferio[0].upper() == "S"):
    if ((mes == 12 and dia >= 21) or mes in (1,2) or (mes == 3 and dia <= 20)):
        print("Verano")
    elif mes in (4,5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif mes in (7,8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")

if (hemisferio[0].upper() == "N"):
    if ((mes == 12 and dia >= 21) or mes in (1,2) or (mes == 3 and dia <= 20)):
        print("Invierno")
    elif mes in (4,5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif mes in (7,8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        print("Verano")
    else:
        print("Otoño")


