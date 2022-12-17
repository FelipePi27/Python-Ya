
##Estructuras Condicionales Anidadas

nota1=int(input("Ingrese primer nota: "))
nota2=int(input("Ingrese segunda nota: "))
nota3=int(input("Ingrese tercer nota: "))
promedio=(nota1+nota2+nota3)/3
if promedio>=5:
    print("Aprobado el curso",(promedio))
else:
    if promedio>=4:
        print("Aprobado con la nota minima",(promedio))
    else:
        print("Reprobado el curso",(promedio))