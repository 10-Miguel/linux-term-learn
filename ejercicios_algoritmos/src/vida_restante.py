print("5)", "Calcular el porcentaje de vida restante: Escribe un algoritmo que solicite la vida máxima y\n la vida actual de un personaje y calcule el porcentaje de vida restante.")
print("Solución")
#empieza el proceso
print("Bienvenido, a continuación vamos a calcular tu vida restante")
a=int(input("Escribe la cantidad de salud total, la barra completa"))
b=int(input("Ahora, dime cuanta salud tienes en este momento y te diré cuánto porcentaje de vida te queda \ncon respecto a tu salud total"))
c=b/a           
d=c*100
print(f"Entonces, te queda un {d:.0f}% de salud")