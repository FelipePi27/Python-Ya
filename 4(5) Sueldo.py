#Estructura de valor secuencial
#Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora

horas=int(input("Ingrese Horas Trabajadas:"))
vht=int(input("Ingrese el valor de una hora de trabajo:"))
#vht=float(input("Ingrese el valor de una hora de trabajo:"))
sueldo= horas*vht
print("El sueldo a pagar es:",(sueldo))

#print(f"El sueldo es:{sueldo:.3f}")