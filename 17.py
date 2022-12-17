
##Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras 
## y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.


print("Bienvenidos")
n=int(input("Ingrese un número entero: "))

if n<10:
    print("El número",n,"tiene un solo digito")
else:
    if n<100:
        print("El número",n,"tiene dos digitos")
    else:
        if n<1000:
            print("El número",n,"tiene tres digitos")
        else:
            print("error al ingresar los datos")
        


        
