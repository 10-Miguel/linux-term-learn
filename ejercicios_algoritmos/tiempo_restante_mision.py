#Calcular el tiempo restante para completar una misión: Escribe un algoritmo que solicite \nel tiempo total de una misión y el tiempo transcurrido, y calcule el tiempo restante para completarla.")
 #Le pediremos al usuario los datos para calcular el resultado final deseado
print("Vamos a averiguar cuánto tiempo te queda para esta misión")
limite_tiempo=float(input("Dime cuál es el límite de minutos que tiene la misión "))
tiempo_gastado=float(input("¿Y cuántos minutos has registrado hasta el momento?"))

#Definimos una variable que será el tiempo restante
tiempo_restante=limite_tiempo-tiempo_gastado

#Le mostramose l resultado al usuario
print(f"Te quedan {tiempo_restante:.1f} minutos para completar la misión")
