
##
#Problema:
#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.


n=int(input("Ingrese cuantos triangulos desea procesar?: "))
catidad=0
for f in range(n):
    base=int(input("Ingrese el valor de la base: "))
    altura=int(input("Ingrese el valor de la altura: "))
    superficie=base*altura/2;
    print ("La superficie del triangilo corresponde a: ",(superficie))

    if superficie > 12:
        catidad=catidad+1
print("La cantidad de tirangilos con superficie mayor a 12 corresponde a: ",(catidad))


