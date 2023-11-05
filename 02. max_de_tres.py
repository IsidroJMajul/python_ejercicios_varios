# 2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

# se declaran las variables VALORES. Con funcion input() para colocar los numeros deseados
valor1 = int(input("El primer valor es: "))
valor2 = int(input("El segundo valor es: "))
valor3 = int(input("El tercer valor es: "))

# se hace la funcion max_de_tres(), con 3 argumentos
def max_de_tres(valor1, valor2, valor3):    
    print("El mayor es: " + str(max(valor1, valor2, valor3)))
    
# ejecutar funcion max_de_tres   
max_de_tres(valor1, valor2, valor3)
    
