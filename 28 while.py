### Estructura repetitiva
##Una estructura repetitiva permite ejecutar una instrucción o un conjunto de instrucciones varias veces.
##Una estructura repetitiva se caracteriza por:
##La sentencia o las sentencias que se repiten.
##El test o prueba de condición antes de cada repetición, que motivará que se repitan o no las instrucciones.

##No debemos confundir la representación gráfica de la estructura repetitiva while (Mientras) con la estructura condicional if (Si)

##Funcionamiento: En primer lugar se verifica la condición, 
# si la misma resulta verdadera se ejecutan las operaciones que indicamos por la rama del Verdadero.
#A la rama del verdadero la graficamos en la parte inferior de la condición. 
# Una línea al final del bloque de repetición la conecta con la parte superior de la estructura repetitiva.
##$En caso que la condición sea Falsa continúa por la rama del Falso 
##y sale de la estructura repetitiva para continuar con la ejecución del algoritmo.
##El bloque se repite MIENTRAS la condición sea Verdadera.
##Importante: Si la condición siempre retorna verdadero estamos en presencia de un ciclo repetitivo infinito. 
#Dicha situación es un error de programación lógico, nunca finalizará el programa.

""" x=1
while x<=100:
    print(x)
    x=x+1 """


x=1
while x<=500:
    print(x)
    x=x+1