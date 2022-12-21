
##Problema:(Promediar)
#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.


suma=0
x=1
n=int(input("Bienvenidos, Ingrese el número de personas a procesar: "))
while x<=n:
    altura=float(input("Ingrese Altura: "))
    suma=suma+altura #operacion de sumar las alturas ingresadas
    x=x+1

promedio=suma/n #operacion de promediar las alturas ingresadas

print("El promedio de altura es: ",(promedio))




##promedio=suma /4
