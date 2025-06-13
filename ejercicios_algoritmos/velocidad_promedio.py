print("7)""Calcular la velocidad promedio de un vehículo en un juego de carreras: Escribe un algoritmo que solicite \nla distancia recorrida y el tiempo tomado, y calcule la velocidad promedio del vehículo.")
print("Solución")# here we go again

#Le pediremos los datos necesarios para calcular su velocidad promedio
print("Ahora vamos a ver a qué velocidad ibas en promedio")
distancia=float(input("¿Recuerdas qué distancia en metros recorriste?"))
tiempo=float(input("Okey, ¿y en cuánto tiempo, en segundos se midió la distancia? Puedes convertir el dato a segundos \nen tiempo_total_juego.py\n"))

#Le mostramos al usuario los datos ingresados
print(f"Sí en {tiempo}s, avanzaste {distancia} metros")

#Definimos una variable que será el resultado de dividir la distancia entre el tiempo
promedio=distancia/tiempo
print(f"Tu velocidad promedio era de {promedio}m/s")
