#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

Nombre=input("Introduzca su nombre")
Horas=int(input("Introduzca su numero de horas"))
Coste=int(input("Introduzca el coste por hora"))
Resultado=Horas*Coste
print(f"Estimado {Nombre},la paga que le corresponde es esta {Resultado}$")