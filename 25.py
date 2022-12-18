
###
##Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
##Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. 
# (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
###
print("Bienvenidos, Ingrese dos números")


x=int(input("Ingrese el primer número: "))
y=int(input("Ingrese el segundo número: "))



if x >0 and y >0:
    print("La coordenada corresponde al cuadrante número 1")
else:
    if x <0 and y >0:
        print("La coordenada corresponde al cuadrante número 2")
    else:
        if x <0 and y <0:
            print("La coordenada corresponde al cuadrante número 3")
        else:
            if x >0 and y <0:
                print("La coordenada corresponde al cuadrante número 4")
            else:
                print("Estas sobre un eje")





