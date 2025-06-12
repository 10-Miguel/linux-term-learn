print("13)""Calcular el porcentaje de misiones completadas: \nEscribe un algoritmo que solicite el número total de misiones y el número de \nmisiones completadas, \ny calcule el porcentaje de misiones completadas.")
print("Solución")#aquí el proceso de nuevo
cantidad_de__misiones=float(input("Bienvenido, para calcular cuantas misiones has completado\ncon respeto al juego, digita la cantidad de misiones totales\n"))
misiones_completadas=float(input("Y cuantas has realizado hasta ahora?\n"))
porcentaje_total1=misiones_completadas/cantidad_de__misiones
porcentaje_total=porcentaje_total1*100
print(f"has complempletado un {porcentaje_total:.1f}%")