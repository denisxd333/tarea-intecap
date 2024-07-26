def contador_de_dinero():
    cantidad_total = 0
    while True:
        print("Contador de Dinero")
        print("------------------")
        print("1. Agregar dinero")
        print("2. Restar dinero")
        print("3. Ver saldo")
        print("4. Salir")
        eleccion = int(input("elija una opcion : "))
        
        if eleccion == 1:
            cantidad = float(input("Ingrese la cantidad a agregar: "))
            cantidad_total += cantidad
            print(f"Agregó ${cantidad:.2f} a su saldo. Nuevo saldo: ${cantidad_total:.2f}")
        elif eleccion == 2:
            cantidad = float(input("Ingrese la cantidad a restar: "))
            if cantidad > cantidad_total:
                print("Saldo insuficiente!")
            else:
                cantidad_total -= cantidad
                print(f"Restó ${cantidad:.2f} de su saldo. Nuevo saldo: ${cantidad_total:.2f}")
        elif eleccion == 3:
            print(f"Su saldo actual es: ${cantidad_total:.2f}")
        elif eleccion == 4:
            print("Saliendo...")
            break
        else:
            print("Elección inválida. Intente de nuevo!")

contador_de_dinero()