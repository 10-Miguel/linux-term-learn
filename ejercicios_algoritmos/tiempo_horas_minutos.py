#"Calcular el tiempo total de juego en horas y minutos: Escribe un algoritmo que solicite el tiempo total jugado en minutos y lo convierta a horas y minutos.")
#proceso

#Le pediremos al usuario el primer dato
minutos=float(input("Bienvenido usuario, para poder calcular el tiempo en horas y minutos\nescribe cuantos minutos jugaste\n"))
#aquí le pido al usuario que escriba cuantos minutos quiere medir
horas=0
#aquí solamente estoy definiendo la variable horas, horas=0, significa que es un cero, un número entero 
if minutos<60:
    #esta condicional me dice que, si el dato que escribe el usuario, es menor que 60...
    print(f"Has jugado por {minutos:.0f} minutos")
    #se imprimirá el dato que escribió exactamente, sin decimales
else:
    #else me dice, que lo que suceda fuera de mi condición puesta en "if", llevará a lo siguiente
    while minutos>=60:
        #mientras (while) para que se repita el proceso, ya que será tipo contador, cada vez que 
        #el dato escrito por el usuario
        #supere el 60, aumentara 1 en horas, y restará 60 de minutos
        horas+=1
        minutos -=60
    print(f"Has jugado por {horas}:{minutos:.0f} minutos")
    #aquí hago que muestre cuantas horas y minutos jugó en formato de (hh:mm)


    #ogganizar secuencial con más variables que se sumen en segundos
        
