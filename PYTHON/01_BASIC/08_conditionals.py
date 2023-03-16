# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=21442

### Conditionals ###

# if syntax

my_condition = False
if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if") # Como le hemos dado una valor false a nuestro print no se ejecutará

my_condition = 5 * 2
if my_condition == 10:
    print("Se ejecuta la condición del segundo if") # Como el resultado es true se ejecutará el print

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")  # Quiere decir: "sino se cumple la condicion anterior, haz esto otro"

my_new_variable = 3
print("It's positive") if my_new_variable > 0 else print("it's negative")

my_new_variable = 0
if my_new_variable > 0:
    if my_new_variable % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif my_new_variable == 0:
    print('A is zero')
else:
    print('A is a negative number')

my_new_variable = 0
if my_new_variable > 0 and my_new_variable % 2 == 0:
        print('A is an even and positive integer')
elif my_new_variable > 0 and my_new_variable % 2 !=  0:
     print('A is a positive integer')
elif my_new_variable == 0:
    print('A is zero')
else:
    print('A is negative')

print("La ejecución continúa")

# Condicional con ispección de valor (con strings)

my_string = "" # Un string vacío es false
if not my_string:
    print("Mi cadena de texto es vacía")
    # Imprime: Mi cadena de texto es vacía

my_string = "Mi cadena de texto"
if my_string:
    print("Mi cadena de texto no es vacía")
    # Imprime: Mi cadena de texto no es vacía

if my_string == "Mi cadena de textoooooo": 
    print("Estas cadenas de texto coinciden")
    # No imprime, porque no coinciden.
