# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

# Importar libreria RANDOM
import random

# crear función "maximo()" para seleccionar nros aleatorios para a y b. Imprimirlos para luego analizarlos.

# Crear funcion
def maximo():
    # asignar 2 variables para que seleccionen valores random (importante: importar libreria RANDOM)
    a = random.randrange(10)
    b = random.randrange(10)
    # imprimir valores seleccionados para las variables A y B
    print (a, b)
    # Hacer CONDICIONAL para que dependiendo del valor de la variable, imprima lo que corresponda
    if a > b:
        print ("Es el primero: ", a)
    elif a == b:
        print("Oops, son iguales *_*")    
    else:
        print("Es el segundo: ", b)    
        
# ejecutar funcion    
maximo()
    
