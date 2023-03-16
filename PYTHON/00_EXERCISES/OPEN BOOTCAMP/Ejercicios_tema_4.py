# Sarai Rodriguez \ Introducción a la programación \ Tema 3 \

### Primera parte ###

# En este ejercicio practicarás las estructuras de control, para ello deberás crear:

# 1- Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
# Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
def condition_if (numeroif:int):
    if numeroif > 0:
        print("It's positive")
    else:
        print("it's negative")
condition_if (3)

# 2- Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
# Incrementar el valor de la variable en uno cada vez que se ejecute.
# Mostrarlo por pantalla cada vez que se ejecute.

numeroWhile = 0
while numeroWhile < 3:
    numeroWhile += 1  # Es una manera avdebiada de escribir: numeroWhile = numeroWhile + 1 (incementa el valor)
    print(numeroWhile)

# dentro de una función:
def condition_while (numeroWhile:int):
    while numeroWhile < 3:
        numeroWhile = numeroWhile + 1
        print(numeroWhile) # Así se meustra el nº resultante de cada vuelta del bucle (1,2,3...)
condition_while(0)

def condition_while_2(numeroWhile: int):
    while numeroWhile < 3:
        numeroWhile = numeroWhile + 1
    print(numeroWhile) # Así se meustra el nº resultante después de dar todas las vueltas del bucle 
condition_while_2(0)

# 3- Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.

numeroWhile = 6
while True: # Mientras sea true se ejecuta el cuerpo
    if numeroWhile < 3: numeroWhile += 1 # Con estos condicionales comprobamos si el resultados cumple lo que queremos
    elif numeroWhile > 3: numeroWhile -=1 # Con estos condicionales comprobamos si el resultados cumple lo que queremos
    else: break
print(numeroWhile)

# dentro de una función dónde el resultado tiene que ser siempre 3 
def condition_do_while(numeroDoWhile: int): # Como no existe el DoWhile en Python. Podemos hacerlo así:
    while True:
        if numeroDoWhile < 3: numeroDoWhile = numeroDoWhile + 1  
        elif numeroDoWhile > 3: numeroDoWhile = numeroDoWhile - 1
        if numeroDoWhile ==3:
            break
    print(numeroDoWhile)
condition_do_while(5)

# 4- Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.

print("VERSION 1")
numero_for = 0
for x in range(6):
    numero_for += 1
    print (numero_for)
    if numero_for >= 3:
        break     

print("VERSION 2") # Ejemplo en el que nos saltamos que se imprima el 2
numero_for = 0
for element in [0,1,2,3,4,5,6]:
    if numero_for < 5: 
        numero_for += 1
    if numero_for != 2:
        print(numero_for)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("VERSION 6")
numero_for = 0
for x in range(4):
    print(numero_for)
    numero_for += 1
print(numero_for)


# 5- Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.