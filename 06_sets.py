## Sets ##

my_set = set()
print(type(my_set))

my_other_set = {}
print(type(my_other_set))            #Inicialmente es un diccionario

my_other_set={"Juan", "Flores", 47}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("devcodebrain")
print(my_other_set)                 # Un Set NO es una estructura ordenada por ende no se puede acceder a un elemento en particular
my_other_set.add("devcodebrain")    #Un Set no admite repetidos
print(my_other_set)

print(my_other_set.__contains__("Juan"))

print("Juan" in my_other_set)

print("Pedro"  in my_other_set)

my_other_set.remove(47)             #Remover un elemento del set, en este caso el dato con valor 47
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

my_set = {"Juan", "Antonio", 1.77}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Switft", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)


