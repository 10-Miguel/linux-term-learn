print("2)", "Calcular el tiempo total de juego: \nEscribe un algoritmo que solicite las horas, minutos y segundos jugados y calcule el tiempo total jugado en segundos.")
print("Solución")
a=int(input("A continuación, escribe '1', si vas a escribir tu tiempo en minutos o escribe '2', si vas a escribir en horas"))
c=0 #Debo definir esta variable para poderla usar al final en la recopilación
e=0
if a==1:
    b=int(input("¿Cuántos minutos?: "))
    c=b*60
    print("Entonces, son", c, "segundos")
    
    
if a==2:
    d=int(input("¿Cuántas horas?: "))
    e=d*3600
    print("Entonces, son", e, "segundos")
else:
    exit()
#Aquí ya hicimos las conversiones, sigue la recopilación de los datos 
print("Entonces si sumaramos todos los segundos, los que pasamos de minutos, y los que pasamos de horas tendriamos un total de")
f= e+c
print(f, "Segundos")