## Listas ##

my_list = list()
my_list.append("Juan")
my_list.append("Flores")
print(my_list)
print(len(my_list))
print(my_list[1])
print(my_list.index("Juan"))


my_other_list = [35,46,62,52,17]
print(my_other_list)
print(len(my_other_list))

my_other_list_1 = [46, 1.76, "Juan", "FLores"] 
print(my_other_list_1)
print(type(my_other_list_1[0]))

age, height, name, surname = my_other_list_1
print(name)

## Sumar Listas
print(my_list + my_other_list)

