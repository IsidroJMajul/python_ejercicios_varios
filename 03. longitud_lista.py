# 3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

# Creamos funcion "longitud(lista)" con un parámetro
def longitud (lista):
    cont = 0    # variable para inicializar un contador
    for i in lista: # hacemos loop, pasando un argumento a "lista"    
        cont += 1   #recorre la lista y suma valor a la variable
    return cont #devuelve nuevo valor de la variable
    
print (longitud('esto es un texto de prueba')) #imprime numero de caracteres
