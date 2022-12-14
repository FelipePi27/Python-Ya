
##Se ingresan tres notas de un alumno, 
## si el promedio es mayor o igual a cinco mostrar un mensaje "Aprobo el Ramo".


print("Bienvenidos, Programa para promediar notas")

nota1=int(input("Ingrese nota 1: "))
nota2=int(input("Ingrese nota 2: "))
nota3=int(input("Ingrese nota 3: "))

notas=nota1+nota2+nota3
promedio=notas/3
if promedio>=5:
    print("Alumno se a eximido: ",(promedio))
else:
    promedio<5
    print("El alumno debe rendir examen: ",(promedio))