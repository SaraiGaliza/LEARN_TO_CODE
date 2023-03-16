# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=32030

### Exception Handling ###

number_one = 5 # Int
number_two = 1 # Int
number_three = "1" # String

# Estructura simple para el contorl de errores: try, except, else, finally.

try:
    print(number_one + number_two)
    print("Not error courred")
except: # Se ejecuta si se prodcue una excepción
    print("Something went wrong")
else:  # Opcional. Se ejecuta si no se produce una excepción
    print("Things go well")
finally:  # Opcional. Se ejecuta siempre haya error o no
    print("Continue wiht this blck")

# Podemos capturar un tipo de error concreto de la sigueinte manera. De esta fomra hacemos que la excepcion se ejecute solo si el tipo de error conincide
try:
    print(number_one + number_three)
    print("Not error courred")
except ValueError: 
    print("Value error occured")
except TypeError:
    print("Type error occured")
except ZeroDivisionError:
    print('zero division error occured')

# También podemos capturar la información de los errorres de las siguientes maneras y así acortamos el código
try:
    print(number_one + number_three)
    print("Not error courred")
except ValueError as e: # Es habitual poner "e" en lugar "error". Es solo el nombre de la variable dónde esta almacenado el error 
    print(e)
except Exception as error: # Así podemos capturar la infomación de cualquier tipo de error. Como el error que estamos tenieindo no es tipo value sino type. No se captura en en el except anterior, pero sí lo capturamos en este.
    print(error)
    
# Ejemplo completo para el control de errores
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError as error:
    print(error)
except Exception as e:
    print(e)
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
