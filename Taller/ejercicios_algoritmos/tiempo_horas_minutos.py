#"Calcular el tiempo total de juego en horas y minutos: Escribe un algoritmo que solicite el tiempo total jugado en minutos y lo convierta a horas y minutos.")
#proceso

#aquí le pido al usuario que escriba cuantas horas jugó
horas=float(input("¿Por cuantas horas jugaste? En caso de que no, escribe 0\n"))

#he aqui convertimos las horas jugadas a segundos
segundos_horas=horas*3600

#he aqui preguntamos los minutos jugados
minutos=float(input("¿Por cuantos minutos jugaste? En caso de que no, escribe 0\n"))

#he aqui convertimos de minutos a segundos
segundos_minutos=minutos*60

#Definimos una variable que sume todos los segundos
segundos=segundos_minutos+segundos_horas

#he aqui mostramos el tiempo jugado en segundos
print(f"Has jugado por: \n{segundos}s")


        
