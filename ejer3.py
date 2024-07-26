def opciones_multiples():
    print("Opciones Múltiples")
    print("------------------")
    eleccion = int(input("Ingrese su elección: "))

    opciones = {
        1: lambda: print("Usted eligió la opción 1"),
        2: lambda: print("Usted eligió la opción 2"),
        3: lambda: print("Usted eligió la opción 3"),
        4: lambda: print("Usted eligió la opción 4"),
        5: lambda: print("Usted eligió la opción 5"),
        "default": lambda: print("Elección inválida. Intente de nuevo!")
    }

    opciones.get(eleccion, opciones["default"])()

opciones_multiples()