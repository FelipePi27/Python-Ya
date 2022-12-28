
###Problema:
#Escribir un programa que solicite por teclado 
#10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 5 y cuántos menores.
#############################################
ma=0
me=0

#print("Bienvenido profesor, Ingrese 10 notas:")

for f in range(10):
    nota=int(input("Ingrese nota: "))
    
    if nota>=5:
        ma=ma+1
    else:
        me=me+1

print("las notas mayores a 5 son: ",(ma))
print("las notas menores a 5 son: ",(me))


    
    




