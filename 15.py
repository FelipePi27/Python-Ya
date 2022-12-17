##Estructuras condicionales anidadas
##Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos


print("Bienvenidos, Ingrese tres números para determinar cúal es mayor")

num1=int(input("Ingrese primer número: "))
num2=int(input("Ingrese segundo número: "))
num3=int(input("Ingrese tercer número: "))

if num1>num2:
    if num1>num3:
        print("El primer número ingresado es el mayor de los tres!")
        print(num1)
    else:
        print("El tercer número ingresado es el mayor de los tres!")
        print(num3)
else:
    if num2>num3:
        print("El segundo número ingresado es el mayor de los tres números!")
        print(num2)
    else:
        print("El tercer número ingresado es el mayor de los tres números!")
        print(num3)


