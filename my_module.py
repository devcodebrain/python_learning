## Functions ##

def my_function():
    print("Esto es una función")

my_function()  # < - Llamado a la función 

def sum_two_values(first_number:int, second_number:int):   #< - Parámetro y tipo de dato
    print("El resultado de la suma es :", first_number + second_number)
sum_two_values(5,7)


def sum_two_values_with_return(first_number:int, second_number:int):   #< - Parámetro y tipo de dato
    my_sum = first_number + second_number 
    return my_sum

my_result =  sum_two_values_with_return(3,4)
print(my_result)

def print_name(name:str, surname:str):
    print(f"{name} {surname}")

print_name("Flores", "Juan")
print_name(surname = "Flores", name = "Juan")

def print_name_with_default(name:str, surname:str, alias:str = "Sin Alias"):   #< - Con valor por default en este caso el Alias
    print(f"{name} {surname} {alias}")

print_name_with_default("Juan", "Flores") # < - la función se ejecuta aunque le pases dos parámetros por que el tercer está definido por default "Sin Alias"
print_name_with_default("Juan", "Flores","devcodebrain")


def print_text(*text):  # al anteponer un * al parámetro significa que le puedes pasar la cantidad parámetros que quieras
    print_text(text)

print("Hola", "Mundo", "Devcodebrain")


def print_texts_capitals(*texts):  # al anteponer un * al parámetro significa que le puedes pasar la cantidad parámetros que quieras
    for element in texts:
        print(element)

print_texts_capitals("Hola", "Mundo", "Devcodebrain")