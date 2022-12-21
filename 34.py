
####Problema:
#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e 
# informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.


#mporte=precio*cantidad

cont1=0
cont2=0
gastos=0
x=1
n=int(input("Bienvenidos, Ingrese el número de EMPLEADOS a procesar: "))
while x<=n:
    sueldo=int(input("Ingrese monto de su SUELDO: "))
    if sueldo<=300:
        cont1=cont1+1
       
    else:
        cont2=cont2+1
    gastos=gastos+sueldo
    x=x+1

print("Cantidad Empleados que su sueldo es menor a 300: ",(cont1))
print("Cantidad Empleados que su sueldo es mayor a 500: ",(cont2))
print("El gasto total en sueldos es: ",(gastos))