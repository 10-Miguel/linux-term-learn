print("3)", "Calcular el daño total causado por un personaje:Escribe un algoritmo que solicite el daño causado por un personaje\n en tres ataques y calcule el daño total.")
print("Solución")#Aquí empieza el proceso
input("Bienvenido, ¿Qué tal?")
daño_ataque1=int(input("Acerca del último nivel, ¿recuerdas cuánto daño hiciste en el primer ataque?"))
daño_ataque2=int(input("Okey, ¿y luego en el segundo ataque?"))
daño_ataque3=int(input("¿Y cuánto daño se registró en el tercer ataque?"))
Total = daño_ataque1+daño_ataque2+daño_ataque3
print("Mmm...")
print(f"Entonces el daño total sería: {daño_ataque1}+{daño_ataque2}+{daño_ataque3}={Total}") #la f string sirve demasiado manito. # Las f-strings permiten insertar-encadenar variables dentro de cadenas de texto de forma sencilla 