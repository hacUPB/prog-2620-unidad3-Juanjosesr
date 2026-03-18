# Solicitar 2 números al usuario e imprimir los valores pares que hay entre dichos números


n1 = int(input("Ingrese el primer número"))
n2 = int(input("Ingrese el segundo número"))

#n1 = 10 y n2 = 25
#n1 = 67 y n2 = 4

#identificar al menor y mayor entre los 2
if n1 > n2:
   mayor = n1
   menor = n2
else:
   mayor = n2
   menor = n1

while mayor >= menor:
    res = mayor % 2   # operador residuo de la división
    if res == 0:
         print(mayor)
    mayor -= 1      #numero = numero - 1