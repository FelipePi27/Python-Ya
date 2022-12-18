
##Problema (Condiciones compuestas con operdores logicos)
##Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
# imprimir en pantalla la leyenda "Alguno de los números es menor a diez".


print("Bienvenidos,Ingrese tres números")

n1=int(input("ingrese el primer valor: "))
n2=int(input("ingrese el segundo valor: "))
n3=int(input("ingrese el tercer valor: "))

if n1<10 or n2<10 or n3<10:
    print("Alguno de los valores ingresados es menor a 10, Intentelo nuevamente")
else:
    print("todos los valores ingresados son igual o mayor a 10")

