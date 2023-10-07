## Tuples ##
## Que es una Tuppla = es un conjunto de valores, la tupla es inmutable##

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35,1.77,"Juan","Flores")
print(type(my_tuple))
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Flores")) #Cuenta las coincidencuas
print(my_tuple.index("Juan"))

#my_tuple[1] =1.80 Error las tuplas son inmutables y son ordenadas, es decir no puedes cambiar el orden de los valores 

my_new_tuple = tuple((1,5,9,3,8,2))
print(my_new_tuple)




