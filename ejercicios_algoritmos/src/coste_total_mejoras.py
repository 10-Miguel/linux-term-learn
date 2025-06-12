print("8)""Calcular el costo total de mejoras en un juego: Escribe un algoritmo que solicite \nel costo de tres mejoras y calcule el costo total de las mejoras.")
print("Solución")#y volvemos con el proceso 
print("Bienvenido.\nA continuación vamos a averiguar el coste total de tus compras")
#Registramos la primera variable como un número decimal (float) y le pedimos al usuario que la digite (input):
primera_factura=float(input("¿Cuánto costó la primera factura?\n"))
segunda_factura=float(input("¿Cuánto costó la segunda factura?\n"))
tercera_factura=float(input("¿Cuánto costó la tercera factura?\n"))
#Despues de que automatizamos el proceso matemático, 
#registramos otra variable para mostrar directamente el resultado invocando esta función:
total=primera_factura+segunda_factura+tercera_factura
print(f"Entonces el precio total de tus compras es\n{primera_factura} + {segunda_factura} + {tercera_factura} \n= {total}")
