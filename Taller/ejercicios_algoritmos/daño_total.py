#3)", "Calcular el daño total causado por un personaje:Escribe un algoritmo que solicite el 
# daño causado por un personaje\n en tres ataques y calcule el daño total.")

#Aquí empieza el proceso
print("Bienvenido, ¿Qué tal estás?\n") #mensaje interactivo no tan necesario

#Vamos a calcular el daño total causado en 3 ataques y le pediremos al usuario que nos entregue los datos
daño_1=int(input("Acerca del último nivel, ¿recuerdas cuánto daño hiciste en el primer ataque?\n"))#pedimos el primer dato
daño_2=int(input("Okey, ¿y luego en el segundo ataque?\n")) #pedimos el segundo dato
daño_3=int(input("¿Y cuánto daño se registró en el tercer ataque?\n"))#pedimos el tercer dato

daño_4=daño_1+daño_2+daño_3 #sumamos todos los datos y a ese resultado le asignamos una variable

print("Mmm...")

#Mostramos el resultado

print(f"Entonces el daño total sería: {daño_1}+{daño_2}+{daño_3}={daño_4}") #la f string sirve demasiado manito. # Las f-strings permiten insertar-encadenar variables dentro de cadenas de texto de forma sencilla 
