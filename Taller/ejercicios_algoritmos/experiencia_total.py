#4)""Calcular la experiencia total ganada: Escribe un algoritmo que solicite la experiencia ganada en tres misiones y calcule la experiencia total acumulada.")
 #aquí empieza el proceso
#Le pido al usuario que me escriba como está en tono de darle animo al programa
#Luego escribirá el primer dato o variable, la segunda y la tercera de manera consecutiva cada vez que envie
#la anterior:

#Vamos a pedirle al usuario los datos para sumarlos
print("¿Cómo estás? A continuación vamos a calcular toda tu experiencia recolectada a lo largo de\nlas últimas 3 misiones")
exp_1no=int(input("¿Cuánto te entregaron respectivamente en cada una?\n"))
exp_2=int(input("\n"))
exp_3=int(input("\n"))

#Ahora definiré la ultima variable para realizar el proceso de suma y listo, luego la invoco para 
#mostrarle al usuario la respuesta

total=exp_1no+exp_2+exp_3
print(f"Amigo, {exp_1no} + {exp_2} + {exp_3 } \n={total}")
