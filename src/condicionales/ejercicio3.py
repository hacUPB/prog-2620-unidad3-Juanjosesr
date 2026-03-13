# Determine si un número ingresado por el usuario es par o impar.

numero = int(input("Ingrese un número: "))

res = numero % 2
if res ==0:
    print("el número ingresado es par")
else:
    print("el número ingresado es impar")