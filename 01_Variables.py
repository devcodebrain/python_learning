#Variables
my_variable = "Juan Antonio Flores Zaher Morales"
last_name = "Flores Zaher Morales"
my_int_variable = 5
my_bool_variable=True


print(my_variable)
print(last_name)
print(my_int_variable)
print(my_bool_variable)


print(my_variable,my_int_variable,my_bool_variable)

#Concatenaciòn de Variables en print()
print("Mi nomnbre  es : ",my_variable)


my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

#Funciones del Sistema
len(my_variable) #len() obtienen la logitud de la variable
print("La longitud de la variable  es :", len(my_variable))

#Variables en una sola lìnea
name,surname,alias,edad = "Juan Antonio","Flores Zaher","devcodebrain",46
print("Mi nombre es :",name,surname,"me encuentras en Github como:", alias,"y tengo", edad,"años de edad")

#Inputs de consola
name = input("Ingresa tu Nombre ")   #< - Espera la entrada del dato por consola del usuario
edad= input("Ingresa tu edad ")
print("Tu nomnre es :",name, "y tu edad es",edad)

#Tipando Variables? en realidad en Python no puedes tipar variables ya que python utiliza tipado dèbil
address :str ="Mi direccion"
peso:int = 45
print(peso)


