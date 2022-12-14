
##Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, 
# en caso contrario informar el producto y la división del primero respecto al segundo.


# print("Ingrese dos valores diferentes")

# num1=int(input("Ingrese el primer valor: "))
# num2=int(input("Ingrese el segundo valor: "))

# if num1>num2:
#     print(num1+num2)
#     print(num1-num2)
# else: 
#     num2>num1
#     print(num1*num2)
#     print(num1/num2)

num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))

if num1>num2:
    suma=num1+num2
    diferencia=num1-num2
    print("La suma de los valores es: ",(suma))
    print("La diferencia es: ",(diferencia))
else:
    producto=num1*num2
    division=num1/num2
    print("El producto es: ",(producto))
    print("La division es: ",(division))


