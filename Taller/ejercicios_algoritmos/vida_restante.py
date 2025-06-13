#5) Calcular el porcentaje de vida restante: Escribe un algoritmo que solicite la vida máxima y la vida actual de un personaje y calcule el porcentaje de vida restante.
#empieza el proceso y le pedimos al usuario que ingrese los datos
print("Bienvenido, a continuación vamos a calcular tu vida restante")
salud_total=int(input("Escribe la cantidad de salud total, la barra completa"))
salud=int(input("Ahora, dime cuanta salud tienes en este momento y te diré cuánto porcentaje de vida te queda \ncon respecto a tu salud total"))
salud_restante=salud/salud_total           

#definimos una nueva variable que será el resultado de la división anterior
salud_restante_1=salud_restante*100
print(f"Entonces, te queda un {salud_restante_1}% de salud")
