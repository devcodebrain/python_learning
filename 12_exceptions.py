## Exception Handling ##

number_one, number_two = 5 ,1 

#number_two = "1"

# try, except
try: 
    print(number_one + number_two)
    print("No ha ocurrido un error ")
except: 
    print("Ocurrió un error ")


# try, except, elese
try: 
    print(number_one + number_two)
    print("No ha ocurrido un error ")
except: 
    # Se ejecuta si se produce una excepción
    print("Ocurrió un error ")
else:
    # Se ejecuta si NO se produce una excepción
    print("Sigue la ejecución continúa correctamente ")
finally:
    # Se ejecuta Siempre, haya o no haya errores
    print("La ejecucuión continúa")

# Captura de excepciones por tipo
try: 
    print(number_one + number_two)
    print("No ha ocurrido un error ")
except ValueError: 
    # Se ejecuta si se produce una excepción
    print("Se ha producido un Value Error ")
except TypeError:
    print("Ocurrió un error de tipo Type Error ")


# Captura de la información de la excepción 
try: 
    print(number_one + number_two)
    print("No ha ocurrido un error ")
except ValueError as error: 
    # Se ejecuta si se produce una excepción
    print("Se ha producido un Value Error ", error)
except Exception as error: 
    # Se ejecuta si se produce una excepción
    print("Se ha producido un Exception Error ", error)
