## Loops/Bucles/Ciclo ##

### While ###

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
print("Terminó el primer bucle")

my_boleano = True

while my_boleano:
    print(my_boleano)
    my_boleano = False
else : # <- Es Opcional
    print("ya es False")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es Igual a 15")
    print("Mi condición es menor que 20", my_condition)


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es Igual a 15")
        break # <- Se detiene la ejecución y se sale del bucle
    print("Mi condición es menor que 20", my_condition)
print("Sigue después del While")


##### For #####


my_list = [35,46,62,52,17]

my_set={"Juan", "Flores", 47}

my_dic= {"Nombre":"Juan", "Surname":"Flores","Edad":46, 1:"Python"}

for element in my_list:
    print(element)

for element in my_set:
    print("Set ", element)

for element in my_dic:
    print("Dicccionario ", my_dic[element])
else:
    print("EL bucle FOR para mi diccionario a finalizado")

for element in my_dic:
    print("Diccionario ", my_dic[element])
    if element == "Edad":
        break
else:
    print("El bucle FOR para mi diccionario a finalizado")