#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad=int(input("Introduzca la cantidad a invertir"))
interes_anual=int(input("Introduzca el interes anual"))
numero_de_años=int(input("Introduzca los años"))
capital_obtenido= cantidad*(1+cantidad)**numero_de_años
print(f"El capital obtenido es {capital_obtenido}")