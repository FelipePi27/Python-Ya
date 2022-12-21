
##
#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe 
# cuántos tienen notas mayores o iguales a 7 y cuántos menores.


na=0   #variable
nb=0   #variable
x=1 #contador

while x <=10: ##contador inicia en x1(menor o igual)
    nota=int(input("Ingrese nota: "))
    if nota>=7:  #condicion positiva
        na=na+1  #nota mayor a 7
    
    else: #condicion negativa
        nb=nb+1 #nota menor a 7
        
    x=x+1 #para que salga del while, que el contador llegue a x10 (número de notas ingresadas)

print("El número de notas altas es: ",(na))#salida
print("El numero de notas bajas es: ",(nb))#salida


                     
    
    
    
    
    