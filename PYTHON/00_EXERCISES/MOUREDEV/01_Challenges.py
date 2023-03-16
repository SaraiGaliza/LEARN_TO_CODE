# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=4142

### Challenges ###

### EJERCICIO 1 ###
# Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".
 # - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

print("EXERCISE 1: START")
def fizz_buzz ():
    for element in (1,101):
        if element % 3 == 0 and element % 5 == 0: # Empezamos por aqui porque e la condición más restrictiva
            print("fizzbuzz")
        elif element %3 == 0: 
            print("fizz")
        elif element %5 == 0:
            print("buzz")
        else:
            print(element)
fizz_buzz()

### EJERCICIO 2 ###
# Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

print("EXERCISE 2: START (First Version)")
def anagram(word_one, word_two):
    return sorted(word_one.lower()) == sorted(word_two.lower())
print(anagram("Amor", "Roma"))


print("EXERCISE 2: START (Second Version)")
def anagram(word_one, word_two):
    return sorted(word_one.lower()) == sorted(word_two.lower())
print(anagram("Zoe", "Onso"))

### EJERCICIO 3 ###
# Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13...

print("EXERCISE 3: START")
def fibonacci():
    previous_1 = 0
    previous_2 = 1
    for element in range (0,50):
        print(previous_1)
        next = previous_1 + previous_2
        previous_1 = previous_2
        previous_2 = next
fibonacci() 

### EJERCICIO 4 ###
# Escribe un programa que se encargue de comprobar si un número es o no primo. Hecho esto, imprime los números primos entre 1 y 100

def is_prime():
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for element in range(2, number):
                if number % element == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)
is_prime()


### EJERCICIO 4 ###
# Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática. Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invertir_texto (texto):
    total_caracteres = len(texto) -1
    resultado_invertido = ""
    for element in (0,total_caracteres):
        resultado_invertido += texto[total_caracteres - element]
    return resultado_invertido
print(invertir_texto("Hola Mundo"))






























def invert_word(word):
    splittedWord = list(word) 
    wordLength = len(splittedWord) - 1
    reversedWord = ''
    while (wordLength >= 0):
        reversedWord += splittedWord[wordLength]
        wordLength-= 1
    print(reversedWord)
invert_word('Hola mundo')

def reverse(text):
    text_len = len(text) - 1
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index]
    return reversed_text
print(reverse("Hola mundo"))
