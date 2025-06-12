print("15)""Calcular el tiempo promedio de una partida: Escribe \nun algoritmo que solicite el tiempo de tres partidas y calcule el tiempo promedio de las partidas.")
print("Solución")#proceso
partida_1=float(input("Bienvenido jugador, para saber en promedio cuanto se tardan 3 partidas,\nescribe a continuación cuántos minutos te tardaste en el primer juego\n"))
partida_2=float(input("Ahora escribe los minutos del segundo juego\n"))
partida_3=float(input("Y los minutos del tercer juego\n"))
tiempo_promedio1=partida_1+partida_2+partida_3
tiempo_promedio=tiempo_promedio1/3
print(f"En promedio cuando juegas 3 partidas seguidas, gastas más o menos {tiempo_promedio:.0f} mins")