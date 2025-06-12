tipo_de_operacion=float(input("Bienvenido a la mejor calculadora. \nDefine si quieres:\n(1) Sumar\n(2) Restar\n(3) Multiplicar\n(4) Dividir\n(5) Potenciar\n")) 
if tipo_de_operacion == 1:

    dato_suma1=float(input("Ingresa la suma:\n"))
    dato_suma2=float(input("+ \n"))
    dato_suma3=float(dato_suma1+dato_suma2)
    print(f"tu resultado es:\n{dato_suma3:.2f}")
    exit()
if tipo_de_operacion==2:
    dato_resta1=float(input("Ingresa la resta\n"))
    dato_resta2=float(input("- \n"))
    dato_resta3=dato_resta1-dato_resta2
    print(f"Tu restultado es: \n{dato_resta3:.2f}")
    exit()
if tipo_de_operacion==3:
    
    dato_multiplica1=float(input("Ingresa tu multiplicación: \n"))
    dato_multiplica2=float(input("x\n"))
    dato_multiplica3=dato_multiplica1*dato_multiplica2
    print(f"Tu resultado es: \n{dato_multiplica3:.2f}")
    exit()
if tipo_de_operacion==4:
    dato_divide1=float(input("Ingresa tu división\n"))
    dato_divide2=float(input("/ \n"))
    dato_divide3=dato_divide1/dato_divide2
    print(f"Tu resultado es: \n{dato_divide3:.4f}")
    exit()
if tipo_de_operacion==5:
    potencia1=float(input("Ingresa la base: \n"))
    potencia2=float(input("Elevada a...: \n"))
    potencia3=float(potencia1**potencia2)
    print(f"Tu resultado es: \n{potencia3}")
    exit()


else:
    print("pailas")

