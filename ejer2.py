def calculadora():
    print("Calculadora")
    print("-----------")
    num1 = float(input("Ingrese el primer número: "))
    operador = input("Ingrese el operador (+, -, *, /): ")
    num2 = float(input("Ingrese el segundo número: "))

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: División por cero!")
            return
    else:
        print("Operador inválido. Intente de nuevo!")
        return

    print(f"Resultado: {resultado:.2f}")

calculadora()