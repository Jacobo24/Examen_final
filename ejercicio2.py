def operacion():
    print("La operacion es: (ax + b) ^n")
    a = int(input("Ingrese el primer numero: "))
    print("Ingrese el primer numero: ")
    b = int(input("Ingrese el segundo numero: "))
    print("Ingrese el segundo numero: ")
    n = int(input("Ingrese el exponente: "))
    x = int(input("Incógnita: "))
    print("Ingrese el exponente: ")

    if n == 0:
        return 1
    elif n == 1:
        return a+b
    elif a == 0:
        return b^n
    elif b == 0:
        return a
    elif a == 1:
        return (1+b)^n
    elif b == 1:
        return a^n
    else:
        return (a*x + b)^n
    expand (a*x + b)^n