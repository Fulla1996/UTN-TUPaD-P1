agenda = {}

for i in range(2):
    hora = (input("Ingrese día del evento: ").lower(), input("Ingrese hora del evento: "))
    evento = input("Cúal es el evento? : ")
    agenda[hora] = evento

print("Ingrese un día y hora para consultar la agenda")

dia = input("Día: ").lower()
hora = input("Hora: ")

print(agenda[(dia, hora)]) if (dia, hora) in agenda else print("Sin actividades")