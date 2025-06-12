print("9)""Calcular el tiempo restante para completar una misión: Escribe un algoritmo que solicite \nel tiempo total de una misión y el tiempo transcurrido, y calcule el tiempo restante para completarla.")
print("Solución") #de nuevo aparece el genio matemático
print("Vamos a averiguar cuánto tiempo te queda para esta misión")
a=float(input("Dime cuál es el límite de minutos que tiene la misión "))
b=float(input("¿Y cuántos minutos has registrado hasta el momento?"))
if b>=20:
    print("Ya se te acabó el tiempo" )
c=a-b
if b<=19:
    print(f"Entonces te quedan {c:.0f} minutos")
