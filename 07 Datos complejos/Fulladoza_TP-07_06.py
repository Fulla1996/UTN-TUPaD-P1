alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del {i+1}° alumno: ")
    alumnos[nombre] = (int(input("Ingrese la primera nota: ")), int(input("Ingrese la segunda nota: ")), int(input("Ingrese la tercera nota: ")))
 
for a in alumnos:
    print(f"{a}: {alumnos[a]} - Promedio: {sum(alumnos[a])/len(alumnos[a]):.2f}")
