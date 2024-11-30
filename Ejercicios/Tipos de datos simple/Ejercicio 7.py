#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

Nombre=input("Introduzca su nombre")
peso=int(input("Introduzca su peso en kg"))
estatura=float(input("Introduzca su estatura en metros"))
Imc=float(peso)/float(estatura**2)
print(f"Estimado {Nombre}, su indice de masa corporal es de {round(Imc,2)}")
