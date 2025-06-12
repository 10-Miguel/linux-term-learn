print("6)""Calcular el oro total recolectado: Escribe un algoritmo que solicite el oro recolectado en tres misiones y calcule \nel oro total acumulado.")
print("Solución")
#y aquí el proceso maluco
print("Bienvenido, para que calculemos cuánto oro recogiste, dime cuantos kilos, no importa si decimales recogiste")
print("En el primer viaje")
a=float(input("")) #aquí debo usar "float" en vez de "int" debido a que el segundo es para enteros, y float sirve para decimales, separados siempre por punto a no ser que use "replace"
print("En el segundo viaje")
b=float(input())
print("Y en el tercer viaje")
c=float(input())
d=a+b+c
print(f"En total, recogiste {a}+{b}+{c}\n={d}k de oro")