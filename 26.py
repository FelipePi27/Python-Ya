
###De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
##a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
##b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
##c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.
######

sueldo=int(input("Ingrese Sueldo: "))
años=int(input("ingrese años trabajados: "))
aumento=sueldo * 0.20
aumento2=sueldo* 0.05



if sueldo <500000 and años >=10:
    print("Se le otorga un aumneto del 20%")
    print("El sueldo a pagar corresponde a: ",(sueldo+aumento))

else:
    if sueldo <500000 and años <10:
        print("Se le otorga un aumento del 5%")
        print("Su sueldo corresponde: ",(sueldo+aumento2))
    else:
        print(sueldo)
            

