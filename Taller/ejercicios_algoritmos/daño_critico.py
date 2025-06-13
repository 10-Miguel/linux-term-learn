#11) Calcular el daño crítico en un ataque: Escribe un algoritmo que solicite el 
# daño base de un ataque y el multiplicador crítico, y calcule el daño crítico.
#Empezamos el proceso aquí

daño_base=float(input("Bienvenido, jugador, para conocer el daño total, por favor escribe el multiplicador que te muestra la pantalla separado por punto\n"))
multiplicador=float(input("Y escbribe también el daño que haces normalmente sin el multiplicador\n"))
 
#Ahora determinamos una nueva variable, que representa el resultado final

daño_total=daño_base*multiplicador
print(f"Tu daño total es \n{daño_total}")
