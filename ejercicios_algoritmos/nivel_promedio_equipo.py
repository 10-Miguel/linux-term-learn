#("10)""Calcular el nivel promedio de un equipo de jugadores: Escribe un algoritmo que solicite el \nnivel de tres jugadores y calcule el nivel promedio del equipo.")
 #aquí el proceso
print("Bienvenidos, a continuación vamos a calcular el nivel promedio del equipo")
print("Jugador 1, digita tu nivel actual")

#Le pediremos al usuario que ingrese los datos
primer_nivel=float(input())
print("Jugador 2, digita tu nivel actual")
segundo_nivel=float(input())
print("Jugador 3, digita tu nivel actual")
tercer_nivel=float(input())
suma_niveles=primer_nivel+segundo_nivel+tercer_nivel

#establezco otra variable que será la respuesta final, que es el promedio entre los 3 datos ingresados

nivel_promedio=suma_niveles/3
print(f"La habilidad en promedio de este equipo es de {nivel_promedio:.1f} niveles")
