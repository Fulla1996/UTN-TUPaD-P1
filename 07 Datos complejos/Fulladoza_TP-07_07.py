def reporte_parciales(aprobados1, aprobados2):
    print(f"Aprobaron ambos parciales{aprobados1.intersection(aprobados2)}")
    print(f"Aprobaron solo un parcial{aprobados1.symmetric_difference(aprobados2)}")
    print(f"Aprobaron al menos un parcial{aprobados1.union(aprobados2)}")



aprobados_parcial_1 = {1,2,3,4,5}
aprobados_parcial_2 = {2,6}

reporte_parciales(aprobados_parcial_1, aprobados_parcial_2)