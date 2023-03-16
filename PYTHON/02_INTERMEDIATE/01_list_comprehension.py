# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=3239
# GitHub 30 Days of Phyton: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/13_Day_List_comprehension/13_list_comprehension.md

### List Comprehension ###
# Es una forma compacta de crear una lista a partir de una secuencia o de otras lsitas (listas, tuplas, rangos, etc.). Es una forma corta de crear una nueva lista.

language = 'Sarai' # Así recorremos un lista
lst = list(language)
print(type(lst))
print(lst)

list = [i for i in language]  # list comprehension
print(type(list))
print(list)

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

# Algunos ejemplos
my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5
my_list = [sum_five(i) for i in range(8)]
print(my_list)
