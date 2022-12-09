import sympy # Importo la libreria sympy

def operacion(a, b, n):
    x = sympy.Symbol('x')
    polinomio = ((a*x+b)^n)
    for i in range(n):
        polinomio += a[i]*x^i
    print("Polinomio: ", polinomio)
    print("Valor en b: ", polinomio.subs(x, b))
    print("Valor en a: ", polinomio.subs(x, a))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]