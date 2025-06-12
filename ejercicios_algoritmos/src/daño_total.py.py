print("3)", "Calcular el daño total causado por un personaje:Escribe un algoritmo que solicite el daño causado por un personaje\n en tres ataques y calcule el daño total.")
print("Solución")#Aquí empieza el proceso
input("Bienvenido, ¿Qué tal estás?\n") #mensaje interactivo no tan necesario
daño1=int(input("Acerca del último nivel, ¿recuerdas cuánto daño hiciste en el primer ataque?\n"))#pedimos el primer dato
daño2=int(input("Okey, ¿y luego en el segundo ataque?\n")) #pedimos el segundo dato
daño3=int(input("¿Y cuánto daño se registró en el tercer ataque?\n"))#pedimos el tercer dato
daño4=daño1+daño2+daño3 #sumamos todos los datos y a ese resultado le asignamos una variable
print("Mmm...")
#Mostramos el resultado
print(f"Entonces el daño total sería: {daño1}+{daño2}+{daño3}={daño4}") #la f string sirve demasiado manito. # Las f-strings permiten insertar-encadenar variables dentro de cadenas de texto de forma sencilla 
