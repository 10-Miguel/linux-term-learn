print("Tarea ejercicios de algoritmos\nPara seleccionar el punto que desea ver\escriba su respectivo número:\n(1) Puntaje total del jugador\n(2) Tiempo total de juego\n(3) Daño total causado por un personaje\n(4) Experiencia total ganada\n(5) Porcentaje de vida restante\n(6) Oro total recolectado\n(7) Velocidad promedio de un vehículo en un juego de carreras\n(8) Costo total de mejoras en un juego\n(9) Tiempo restante para completar una misión\n(10) Nivel promedio de un equipo de jugadores\n(11) Calcular el multiplicador de daño crítico\n(12) Tiempo total de juego en horas y minutos\n(13) Porcentaje de misiones completadas\n(14) Costo total de objetos comprados en una tienda del juego\n(15) Tiempo promedio de una partida\n(16) Porcentaje de enemigos derrotados")

#Le pedimos al usuario que escriba el punto del ejercicio que desea revisar
punto=float(input())
if punto == 1:
    #"1)", " Calcular el puntaje total de un jugador; escribe un algoritmo que solicite\nlos puntos obtenidos en 3 niveles de un videojuego y calcule el puntaje total\ndel jugador")
    # no sé que hacer ya xd
     print("Solución") #aquí empieza el proceso
     # Vamos a mostrarle un mensaje al usuario de que queremos pedirle, y luego el va a digitar los datos
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



if punto==2:
    #Calcular el tiempo total de juego: \nEscribe un algoritmo que solicite las horas, minutos y segundos jugados y calcule el tiempo total jugado en segundos.")
    horas=float(input("A continuación, escribe tu tiempo en horas"))
    
    #Debo definir esta variable para poderla usar al final en la recopilación y mostrar el resultado desead
    segundos= horas*3600

    #Mostramos el resultado en segundos
    print(f"{segundos} segundos")



if punto==3:
    #3)", "Calcular el daño total causado por un personaje:Escribe un algoritmo que solicite el 
    # daño causado por un personaje\n en tres ataques y calcule el daño total.")
    # #Aquí empieza el proceso
    print("Bienvenido, ¿Qué tal estás?\n") #mensaje interactivo no tan necesario
    
    # Vamos a calcular el daño total causado en 3 ataques y le pediremos al usuario que nos entregue los datos
    daño_1=int(input("Acerca del último nivel, ¿recuerdas cuánto daño hiciste en el primer ataque?\n"))#pedimos el primer dato
    daño_2=int(input("Okey, ¿y luego en el segundo ataque?\n")) #pedimos el segundo dato
    daño_3=int(input("¿Y cuánto daño se registró en el tercer ataque?\n"))#pedimos el tercer dato
    
    daño_4=daño_1+daño_2+daño_3 #sumamos todos los datos y a ese resultado le asignamos una variable
    print("Mmm...")
    
    #Mostramos el resultado
    print(f"Entonces el daño total sería: {daño_1}+{daño_2}+{daño_3}={daño_4}") #la f string sirve demasiado manito. # Las f-strings permiten insertar-encadenar variables dentro de cadenas de texto de forma sencilla 

if punto==4:
    #4)""Calcular la experiencia total ganada: Escribe un algoritmo que solicite la experiencia 
    #ganada en tres misiones y calcule la experiencia total acumulada
    #aquí empieza el proceso

    # #Luego escribirá el primer dato o variable, la segunda y la tercera de manera consecutiva cada vez 
    # que envie la anterior:
    # #Vamos a pedirle al usuario los datos para sumarlos
    print("¿Cómo estás? A continuación vamos a calcular toda tu experiencia recolectada a lo largo de\nlas últimas 3 misiones")
    exp_1no=int(input("¿Cuánto te entregaron respectivamente en cada una?\n"))
    exp_2=int(input("\n"))
    exp_3=int(input("\n"))
    
    #Ahora definiré la ultima variable para realizar el proceso de suma y listo, luego la invoco para
    #mostrarle al usuario la respuesta
    total=exp_1no+exp_2+exp_3
    print(f"Amigo, {exp_1no} + {exp_2} + {exp_3 } \n={total}")

if punto==5:
    #5) Calcular el porcentaje de vida restante: Escribe un algoritmo que solicite la vida máxima y la vida actual de un personaje y calcule el porcentaje de vida restante.
    #empieza el proceso y le pedimos al usuario que ingrese los datos
    print("Bienvenido, a continuación vamos a calcular tu vida restante")
    salud_total=int(input("Escribe la cantidad de salud total, la barra completa"))
    salud=int(input("Ahora, dime cuanta salud tienes en este momento y te diré cuánto porcentaje de vida te queda \ncon respecto a tu salud total"))
    salud_restante=salud/salud_total  

    #definimos una nueva variable que será el resultado de la división anterior
    # salud_restante_1=salud_restante*100
    print(f"Entonces, te queda un {salud_restante}% de salud")

if punto==6:
    #Calcular el oro total recolectado: Escribe un algoritmo que solicite el oro recolectado en tres misiones y calcule \nel oro total acumulado.")
    #y aquí el proceso 
    print("Bienvenido, para que calculemos cuánto oro recogiste, dime cuantos kilos, no importa si decimales recogiste")
    
    #aqui empezamos a recolectar los datos
    print("En el primer viaje")
    peso1=float(input()) #aquí debo usar "float" en vez de "int" debido a que el segundo es para enteros, y float sirve para decimales, separados siempre por punto a no ser que use "replace"
    print("En el segundo viaje")
    peso2=float(input())
    print("Y en el tercer viaje")
    peso3=float(input())
    #sumamos los datos
    peso4=peso1+peso2+peso3
    
    #mostramos el resultado
    print(f"En total, recogiste {peso1}+{peso2}+{peso3}\n={peso4}k de oro")


if punto==7:
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

if punto==8:
    #Calcular el costo total de mejoras en un juego: Escribe un algoritmo que solicite \nel costo de tres mejoras y calcule el costo total de las mejoras.
    #y volvemos con el proceso 
    print("Bienvenido.\nA continuación vamos a averiguar el coste total de tus compras")
    
    #Registramos la primera variable como un número decimal (float) y le pedimos al usuario que la digite (input):
    primera_factura=float(input("¿Cuánto costó la primera factura?\n"))
    segunda_factura=float(input("¿Cuánto costó la segunda factura?\n"))
    tercera_factura=float(input("¿Cuánto costó la tercera factura?\n"))
    
    #Despues de que automatizamos el proceso matemático, 
    #registramos otra variable para mostrar directamente el resultado invocando esta función:
    total=primera_factura+segunda_factura+tercera_factura
    print(f"Entonces el precio total de tus compras es\n{primera_factura} + {segunda_factura} + {tercera_factura} \n= {total}")

if punto == 9:
   #(9)Calcular el tiempo restante para completar una misión: Escribe un algoritmo que solicite \nel tiempo total de una misión y el tiempo transcurrido, y calcule el tiempo restante para completarla.")
   # #Le pediremos al usuario los datos para calcular el resultado final deseado
   print("Vamos a averiguar cuánto tiempo te queda para esta misión")
   limite_tiempo=float(input("Dime cuál es el límite de minutos que tiene la misión "))
   tiempo_gastado=float(input("¿Y cuántos minutos has registrado hasta el momento?"))
   
   #Definimos una variable que será el tiempo restante
   tiempo_restante=limite_tiempo-tiempo_gastado
   
   #Le mostramose l resultado al usuario
   print(f"Te quedan {tiempo_restante:.1f} minutos para completar la misión")


if punto == 10:
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
    
    # #establezco otra variable que será la respuesta final, que es el promedio entre los 3 datos ingresados
    nivel_promedio=suma_niveles/3
    print(f"La habilidad en promedio de este equipo es de {nivel_promedio:.1f} niveles")

if punto==11:
    #11) Calcular el daño crítico en un ataque: Escribe un algoritmo que solicite el 
    # daño base de un ataque y el multiplicador crítico, y calcule el daño crítico.
    #Empezamos el proceso aquí
    
    #Le pediremos al usuario que escriba los datos para hacer los procesos
    daño_base=float(input("Bienvenido, jugador, para conocer el daño total, por favor escribe el multiplicador que te muestra la pantalla separado por punto\n"))
    multiplicador=float(input("Y escbribe también el daño que haces normalmente sin el multiplicador\n"))
    
    #Ahora determinamos una nueva variable, que representa el resultado final
    daño_total=daño_base*multiplicador
    print(f"Tu daño total es \n{daño_total}")


if punto == 12:
    #(12)Calcular el tiempo total de juego en horas y minutos: Escribe un algoritmo que solicite el tiempo total jugado en minutos y lo convierta a horas y minutos.")
    #proceso
    
    # aquí le pido al usuario que escriba cuantas horas jugó
    horas=float(input("¿Por cuantas horas jugaste? En caso de que no, escribe 0\n"))
    
    #he aqui convertimos las horas jugadas a segundos
    segundos_horas=horas*3600

    #he aqui preguntamos los minutos jugados
    minutos=float(input("¿Por cuantos minutos jugaste? En caso de que no, escribe 0\n"))
    
    #he aqui convertimos de minutos a segundos
    segundos_minutos=minutos*60
    
    #Definimos una variable que sume todos los segundo
    segundos=segundos_minutos+segundos_horas
    #he aqui mostramos el tiempo jugado en segundos
    print(f"Has jugado por: \n{segundos}s")


        



if punto == 13:
    #(13)"Calcular el porcentaje de misiones completadas: \nEscribe un algoritmo que solicite el número total de misiones y el número de \nmisiones completadas, \ny calcule el porcentaje de misiones completadas.")
    
    #Le pedimos al usuario los datos
    cantidad_de__misiones=float(input("Bienvenido, para calcular cuantas misiones has completado\ncon respeto al juego, digita la cantidad de misiones totales\n"))
    misiones_completadas=float(input("Y cuantas has realizado hasta ahora?\n"))
    
    #Definimos una nueva variable para mostrar el porcentaje decimal
    porcentaje_total1=misiones_completadas/cantidad_de__misiones
    
    #Definimos otra variable para mostrar el porcentaje en entero
    porcentaje_total=porcentaje_total1*100
    print(f"has complempletado un {porcentaje_total:.1f}%")

if punto == 14:
    #Calcular el costo total de objetos comprados en una tienda del juego: Escribe un algoritmo que solicite 
    # el costo de tres objetos comprados en una tienda del juego y calcule el costo total.
    #proceso

    #Le vamos a pedir al usuario los 3 valores, y determinaremos que esos valores serán decimales por si 
    #nos entregan datos decimales, con la función float
    compra_1=int(input("Bienvenido a la tienda del juego, jugador, a continuación digita el coste de tu primera compra \n"))
    compra_2=int(input("Y el costo de la segunda \n"))
    compra_3=int(input("¿La tercera? \n"))
    
    #Ahora determinaré que total, es una variable, que resulta de la suma de los 3 valores digitados por el usuario
    #para luego invocar esa variable y mostrar el precio total directamente
    total=compra_1+compra_2+compra_3
    print(f"Entonces, el costo total de la compra es \n${total}")

if punto == 15:
    #(15)Calcular el tiempo promedio de una partida: Escribe \nun algoritmo que solicite el tiempo de tres partidas y calcule el tiempo promedio de las partidas.")
    #proceso de registrar los datos, pidiendoselos al usuario
    partida_1=float(input("Bienvenido jugador, para saber en promedio cuanto se tardan 3 partidas,\nescribe a continuación cuántos minutos te tardaste en el primer juego\n"))
    partida_2=float(input("Ahora escribe los minutos del segundo juego\n"))
    partida_3=float(input("Y los minutos del tercer juego\n"))
    
    #definimos una variable que será el resultado de la suma de los 3 datos ingresados
    tiempo_promedio1=partida_1+partida_2+partida_3
    
    #definimos otra variable que será el resultado de dividir la suma de los 3 datos ingresados entre 
    tiempo_promedio=tiempo_promedio1/3
    
    #mostramos el resultado final al usuario
    print(f"En promedio cuando juegas 3 partidas seguidas, gastas más o menos {tiempo_promedio:.0f} mins")


if punto == 16:
    #"16)""Calcular el porcentaje de enemigos derrotados: Escribe un algoritmo que solicite el número total de enemigos y el número de enemigos derrotados, y calcule el porcentaje de enemigos derrotados."
    # #proceso

    # aquí vamos a empezar a recolectar los datos del usuario y a definir que esos datos son decimales
    enemigos_totales=float(input("Bienvenido, para conocer tu progreso\nescribe la cantidad total de enemigos que habian al principio\n"))
    enemigos_derrotados=float(input("¿Y cuantos has derrotado?\n"))
    
    #aquí definimos una nueva variable para el resultado de la división de los datos
    porcentaje_derrotados1=enemigos_derrotados/enemigos_totales
    
    #y aquí hacemos otra variable para mostrar el resultado en porcentaje, 1f(1 decimal)
    porcentaje_derrotados=porcentaje_derrotados1*100
    #mostramos el resultado final
    print(f"Llevas un progreso del {porcentaje_derrotados:.1f}%")


