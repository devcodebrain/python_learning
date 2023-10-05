## Strings ##

my_string = "Mi string"
my_other_string = 'Mi otro string'
print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \n con salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

## Formateo de Strings ##

name, surname, age = "Juan", "Flores", 46

## Ejemplo de Formateo con .format ##
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))

## Ejemplo de Formateo con parseo de variables
## %s para strings  %d para Enteros %f para flotantes
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))

## Inferencia de datos se pone una f minúscula al principio del mensaje
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

## Unpacking characters
language = "python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

## División 
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

## Reverse Languaje
reversed_languaje = language[::-1]
print(reversed_languaje)

## Funciones del Sistema
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))
print(language.replace("t","r"))
