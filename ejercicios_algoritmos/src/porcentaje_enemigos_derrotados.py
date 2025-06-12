print("16)""Calcular el porcentaje de enemigos derrotados: Escribe un algoritmo que solicite el número total de enemigos y el número de enemigos derrotados, y calcule el porcentaje de enemigos derrotados.")
print("Solución")#proceso
#Aquí vamos a empezar a recolectar los datos del usuario y a definir que esos datos son decimales
enemigos_totales=float(input("Bienvenido, para conocer tu progreso\nescribe la cantidad total de enemigos que habian al principio\n"))
enemigos_derrotados=float(input("¿Y cuantos has derrotado?\n"))
#aquí definimos una nueva variable para el resultado de la división de los datos
porcentaje_derrotados1=enemigos_derrotados/enemigos_totales
#y aquí hacemos otra variable para mostrar el resultado en porcentaje, 1f(1 decimal)
porcentaje_derrotados=porcentaje_derrotados1*100
print(f"Llevas un progreso del {porcentaje_derrotados:.1f}%")
