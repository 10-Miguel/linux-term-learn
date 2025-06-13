#(15)Calcular el tiempo promedio de una partida: Escribe \nun algoritmo que solicite el tiempo de tres partidas y calcule el tiempo promedio de las partidas.")
#proceso de registrar los datos, pidiendoselos al usuario

partida_1=float(input("Bienvenido jugador, para saber en promedio cuanto se tardan 3 partidas,\nescribe a continuación cuántos minutos te tardaste en el primer juego\n"))
partida_2=float(input("Ahora escribe los minutos del segundo juego\n"))
partida_3=float(input("Y los minutos del tercer juego\n"))

#definimos una variable que será el resultado de la suma de los 3 datos ingresados
tiempo_promedio1=partida_1+partida_2+partida_3

#definimos otra variable que será el resultado de dividir la suma de los 3 datos ingresados entre 3
tiempo_promedio=tiempo_promedio1/3

#mostramos el resultado final al usuario
print(f"En promedio cuando juegas 3 partidas seguidas, gastas más o menos {tiempo_promedio:.0f} mins")
