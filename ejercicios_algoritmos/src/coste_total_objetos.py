print("14)""Calcular el costo total de objetos comprados en una tienda del juego: Escribe un algoritmo que solicite el costo de tres objetos comprados en una tienda del juego y calcule el costo total.")
print("Solución")#proceso
#Le vamos a pedir al usuario los 3 valores, y determinaremos que esos valores serán decimales por si 
#nos entregan datos decimales, con la función float
compra_1=int(input("Bienvenido a la tienda del juego, jugador, a continuación digita el coste de tu primera compra \n"))
compra_2=int(input("Y el costo de la segunda \n"))
compra_3=int(input("¿La tercera? \n"))
#Ahora determinaré que total, es una variable, que resulta de la suma de los 3 valores digitados por el usuario
#, para luego invocar esa variable y mostrar el precio total directamente
total=compra_1+compra_2+compra_3
print(f"Entonces, el costo total de la compra es \n${total}")
