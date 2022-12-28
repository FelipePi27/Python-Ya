
###
#Problema:
#Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional 
# (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
# if valor%2==0:

##################

pares=0
impares=0
x=1

n=int(input("Ingrese cuantos números desea procesar: "))
while x<=n:
    valor=int(input("Ingrese un número: "))
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
    
    x=x+1

print("la cantidad de númerpos pares es: ",(pares))
print("la cantidad de númerpos impares es: ",(impares))



