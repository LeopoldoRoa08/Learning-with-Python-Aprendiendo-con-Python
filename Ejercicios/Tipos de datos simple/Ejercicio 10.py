#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

g_payasos=int(112)
g_muñecas=int(75)
n_payasos=int(input("Introduzca el numero de payasos"))
n_muñecas=int(input("Introduzca el numero de muñecas"))
peso_total_muñecas=g_muñecas*n_muñecas
peso_total_payasos=g_payasos*n_payasos
print(f"El numero de muñecas vendidas es {n_muñecas}, y el de payasos es {n_payasos}.El peso total de los payasos es {peso_total_payasos}, el de muñecas es {peso_total_muñecas}")