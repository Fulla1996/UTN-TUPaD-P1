def segundos_a_horas(segundos):
    print(f"{segundos} segundos son {segundos/3600:.2f} horas")

seg = int(input("Ingrese cantidad de segundos para su conversión: "))

segundos_a_horas(seg)