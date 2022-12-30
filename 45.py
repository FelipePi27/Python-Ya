
#Problema:
#Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. 
#Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
#####################################################################################3

mul_T=0
mul_C=0
for f in range(10):
    
    n=int(input("Ingrese un número: "))
    if n%3==0:
        mul_T=mul_T+1
    if n%5==0:
        mul_C=mul_C+1

print("La cantidad de numeros ingresados que son multiplo de 3 es: ",(mul_T))
print("La cantidad de numeros ingresados que son multiplo de 5 es: ",(mul_C))
    


    
    