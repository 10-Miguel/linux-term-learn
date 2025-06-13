
#"1)", " Calcular el puntaje total de un jugador; escribe un algoritmo que solicite\nlos puntos obtenidos en 3 niveles de un videojuego y calcule el puntaje total\ndel jugador")
#no sé que hacer ya xd

print("Solución") #aquí empieza el proceso

#Vamos a mostrarle un mensaje al usuario de que queremos pedirle, y luego el va a digitar los datos
print("Bienvenido jugador, a continuación vamos a calcular tu puntaje total")
puntos1=int(input("¿Cuántos puntos obtuviste en el primer nivel?\n"))
print(puntos1)
puntos2=int(input("¿Cuántos puntos obtuviste en el segundo nivel?\n"))
print(puntos2)
puntos3=int(input("¿Cuántos puntos obtuviste en el tercer nivel?\n"))
print(puntos3)

#Aquí le explicamos el proceso, aunque no es necesario
print("Bueno, es fácil, vamos a sumar", (puntos1), "+", (puntos2),"+",(puntos3))

#definimos una nueva variable que muestra la respuesta final
puntos4 = puntos1+puntos2+puntos3 #Aquí defino una variable para mostrar la respuesta que el usuario quiere, que es sumar los datos anteriores

#y aquí  invoco directamente la respuesta
print("El resultado es\n",(puntos4), "felicitaciones")
