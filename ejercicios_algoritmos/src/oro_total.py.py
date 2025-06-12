print("6)""Calcular el oro total recolectado: Escribe un algoritmo que solicite el oro recolectado en tres misiones y calcule \nel oro total acumulado.")
print("Solución")
#y aquí el proceso maluco
print("Bienvenido, para que calculemos cuánto oro recogiste, dime cuantos kilos, no importa si decimales recogiste")
#aqui empezamos a recolectar los datos
print("En el primer viaje")
peso1=float(input()) #aquí debo usar "float" en vez de "int" debido a que el segundo es para enteros, y float sirve para decimales, separados siempre por punto a no ser que use "replace"
print("En el segundo viaje")
peso2=float(input())
print("Y en el tercer viaje")
peso3=float(input())
#sumamos los datos
peso4=peso1+peso2+peso3
print(f"En total, recogiste {peso1}+{peso2}+{peso3}\n={peso4}k de oro")
