# Programa para adivinar un numero dado por la base de datos

from random import *

# Input

Numero = int(input("Digite un numero del 0 al 10: "))

# Processing

x = randint (0,10)

if x == Numero:
    print ("Tu numero" , Numero , "ha sido acertado")
elif x < Numero:
    print ("Tu numero" , Numero , "esta un poco arriba," , x , "es el numero que estabas buscando")
else:
    print ("Tu numero" , Numero , "esta un poco abajo," , x , "es el numero que estabas buscando")