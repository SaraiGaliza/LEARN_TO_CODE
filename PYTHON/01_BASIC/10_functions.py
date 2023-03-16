# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

### Functions ###
# Nos sirven para agrupar código
# Para definir o declarar una función, Python proporciona la palabra clave def. El bloque de código de la función se ejecuta sólo si la función es llamada o invocada
# Cuando creamos una función, la llamamos declarando una función. Cuando empezamos a usarla, la llamamos llamar o invocar una función. Una función puede declararse con o sin parámetros
# Pueden definirser con parámetros o sin parámetros

# Así se declara una función. Todo lo que tengamos tabulado dentro de la funccion pertenecerá a la funcion.
def function_01():
    print("Esto es un ejemplo de función")
     #function_01() # No hacer esto, ya que estaríamos creando un bucle infinito
# Así se llama a la funcion definida anteriormente. Si la funcion no se llama, no se muestra.
function_01()

# Ejmplo 1 de función sin parámetros con strings
def function_full_name():
    first_name = 'Sarai'
    last_name = 'Rodriguez'
    space = ' ' # OJO! También hay que llamar a los especacios
    full_name = first_name + space + last_name # Ahora podemos concatenar las variables anteriores en una nueva variable
    print(full_name) # Y definir que el resultado 
function_full_name()  # Finalmente llamamos al resultado de la funcion

# Ejemplo 2 de función sin parámetios con int
def function_sum_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
function_sum_numbers()

# Función con parámetros de entrada/argumentos
def sum_two_values(first_value: int, second_value): #especificar aqui un int, no vale de nada a nivel de operaciones porque a la hora de llamar la funcion el tipo de dato se reescribirá por el valor que le asignemos en ese momento
    print(first_value + second_value)
sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7") # si la operacion de la función fuese una division, esto daría error porque los strings no aceptan esta operación
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno. ESTO NO LO ENTIENDO
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum 
my_result = sum_two_values_with_return(10, 5) # Para llamar a la funcion, tenemos que asignarla a una variable
print(my_result)

# Función con parámetros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}") #Con la f" accedemos a los valores de los corchetes, sin ella imprimiría tal cual lo que está en el medio de las comillas
print_name(surname="Rodriguez", name="Sarai")

# Función con parámetros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default("Sarai", "Rodriguez") # En este caso imprime "Sin alias"
print_name_with_default("Sarai", "Rodriguez", "Mindfungaziña") # En este se sobreescribe MureDev en el alias

# Función con parámetros de entrada/argumentos arbitrarios
def print_upper_texts(*texts): # De esta forma podemos pasar varios parámetos
    print(type(texts))
    for text in texts:
        print(text.upper())
print_upper_texts("Hola", "Python", "Zoe es la mejor")
print_upper_texts("Hola")


### EXERCISES OPEN BOOTCAMP ###

#  1- Crear una función con tres parámetros que sean números que se suman entre sí + llamar a la función en el main y darle valores.

# Ejemplo con print dentro de la funcion
def function_with_3_strings(param_1, param_2, param_3):
    complete_name = param_1 + param_2 + param_3
    print(complete_name)  # Devuelve: SaraiRodriguezLago
function_with_3_strings("Sarai", "Rodriguez", "Lago")

# Ejemplo con print dentro de la funcion y tipado de dato
def function_with_3_int(param_1: int, param_2: int, param_3: float):
    return (param_1 + param_2 + param_3)
result = function_with_3_int(5, 10, 10.5)
print(result)  # Devuelve: 24.5


### EXERCISES 30 DAYS OF PUTHON - LEVEL 1 ###

# 1- Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers():
    number_01 = 10 # Así añadimos nosotros los números
    number_02 = 5.5
    print (number_01 + number_02)
add_two_numbers ()

def add_two_numbers_version_2 (ex_01_num_01, ex_01_num_02):
    print (ex_01_num_01 + ex_01_num_02)
add_two_numbers_version_2 (10, 5.5) # Asi "llamamos" a dos numeros

# 2- Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math
def area_of_circle(ex_02_radio):
    area = math.pi * (ex_02_radio * ex_02_radio)
    print (area)
area_of_circle(6)

# 3- Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(ex_04_value_01, ex_04_value_02, ex_04_value_03):
    print(ex_04_value_01 + ex_04_value_02 + ex_04_value_03)
    print(type(ex_04_value_01 + ex_04_value_02 + ex_04_value_03))
add_all_nums(1,2,3)

# 4- Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(ex_04_grados):
    conversor_celisus = (ex_04_grados * 9 / 5) + 32
    print (conversor_celisus)
convert_celsius_to_fahrenheit (30)

# 5- Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(ex_05_month):
    if ex_05_month <= 3:
        print("winter")
    if ex_05_month >= 4 and ex_05_month <= 6:
        print("spring")
    if ex_05_month >= 7 and ex_05_month <= 9:
        print("autumn")
    if ex_05_month >= 10 and ex_05_month <= 12:
        print("summer")
check_season (9)

# 6- Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(valor):
   equation = valor
   return equation
ex_06_solution = calculate_slope (30)
print (ex_06_solution)

# 7- Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

# 8- Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
