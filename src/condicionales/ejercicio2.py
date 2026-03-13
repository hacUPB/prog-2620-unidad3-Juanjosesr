# Resuelve el siguiente problema usando el condicional simple.

# Un almacén cobra `$9 000` por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a `$100 000`. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.


compra = int(input("ingrese el precio de la compra"))
Total = compra
if compra < 100000:
    Total = compra + 9000
    print(Total)
print(Total)