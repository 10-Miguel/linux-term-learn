print("16)""Calcular el porcentaje de enemigos derrotados: Escribe un algoritmo que solicite el número total de enemigos y el número de enemigos derrotados, y calcule el porcentaje de enemigos derrotados.")
print("Solución")#proceso
enemigos_totales=float(input("Bienvenido, para conocer tu progreso\nescribe la cantidad total de enemigos que habian al principio"))
enemigos_derrotados=float(input("¿Y cuantos has derrotado?"))
porcentaje_derrotados1=enemigos_derrotados/enemigos_totales
porcentaje_derrotados=porcentaje_derrotados1*100
print(f"Llevas un progreso del {porcentaje_derrotados:.1f}%")
