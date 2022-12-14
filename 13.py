
##Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos.
##(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)


print("Bienvenidos, Ingrese un número entre el 1 y el 99")
num=int(input("Ingrese un número: "))

if num <=9:
    print("El número ingresado tiene un digito")

else:
    print("El número ingresado tiene dos digitos")
