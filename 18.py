
##Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
##cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. 
##Se pide confeccionar un programa que ingrese los dos datos por teclado e 
##informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:

##Nivel máximo:	Porcentaje>=90%.
##Nivel medio:	Porcentaje>=75% y <90%.
##Nivel regular: Porcentaje>=50% y <75%.
##Fuera de nivel: Porcentaje<50%.

print("Bienvenidos")
Total_preguntas=int(input("Ingrese número total de preguntas : "))
Total_correctas=int(input("Ingrese número total de respuestas correctas : "))

Porcentaje=Total_correctas * 100 // Total_preguntas


if Porcentaje>=90:
    print("nivel maxim0 de porcentaje")
else:
    if Porcentaje>=75:
        print("nivel medio de porcentaje")
    else:
        if Porcentaje>=50:
            print("nivel regular de porcentaje")
        else:
            print("El porcentaje obtenido no es suficiente")
            



