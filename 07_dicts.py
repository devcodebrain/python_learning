## Dictionaries ##
my_dict = dict()
print(type(my_dict))

my_other_dic = {}
print(type(my_other_dic))

my_other_dic= {"Nombre":"Juan", "Surname":"Flores","Edad":46, 1:"Python"}
print(my_other_dic)

my_dict = {
    "Nombre":"Juan",
    "Surname":"Flores",
    "Edad":13,
    "Lenguajes":{"Python","Swift","C#"},
    1:1.77
    }
print(my_dict)
print(my_dict["Nombre"])               ## Acceder al valor de un elemento utilizando el Key del mismo

my_dict["Nombre"] = "Malú"             ## Modificar el valor de un Key determinado
print(my_dict["Nombre"])

my_dict["Calle"] = "Privada la Finca"  ## Añade un valor al diccionario en el key Calle
print(my_dict)

del my_dict["Calle"]                   ## Elimianr un elemento del Diccionario
print(my_dict)

print(my_dict.items())  # Retorna todo el Diccionario en Formato Clave Valor
print(my_dict.keys())   # Retorna solamente las Claves (Keys)
print(my_dict.values()) # Retorna solamente los valores

my_new_dict = my_dict.fromkeys(my_dict) ## Copia de otro diccionario pero solo sus llaves SIN valores
print(my_new_dict)

