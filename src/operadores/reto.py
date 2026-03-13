#  🏆 **Reto Final: El Validador de Videojuegos**
 
 
#  Estás programando la lógica de una tienda de videojuegos en línea. Un usuario quiere comprar un juego de clasificación "M" (Mature / Para mayores de 17 años) que cuesta $60.
 
#  Crea un programa que declare las siguientes variables:
 
#  - `edad_usuario` (asigna un número)
#  - `saldo_billetera` (asigna un número decimal)
#  - `tiene_suscripcion_premium` (asigna `True` o `False`)
 
#  Tu programa debe evaluar y guardar en una variable llamada `compra_exitosa` (que será True o False) si el usuario puede comprar el juego.
 
#  **Condiciones para que la compra sea exitosa:**
 
#  1. El usuario debe tener al menos 17 años.
#  2. El usuario debe tener suficiente saldo en su billetera. ¡Pero atención! Si tiene suscripción premium, el juego tiene un 10% de descuento.
 
#  *Pista: Primero calcula el precio final usando operadores aritméticos y luego evalúa la lógica con operadores relacionales y lógicos.*
 
#  📤 **Acción en Bitácora:** Sube el código de tu Reto Final a tu repositorio en un archivo llamado `reto_operadores.py`. En tu archivo Markdown de bitácora, explica brevemente qué se te dificultó más de este reto y cómo lo resolviste. ¡Mucho éxito!

edad_usuario = float(input("ingrese su edad:"))
saldo_billetera = float(input("ingrese su dinero:"))
tiene_suscripcion_premium = input("Cuenta con la suscrición premium:")

Precio = 60
Precio_suscripción = 60 * 0.1

compra_exitosa = (edad_usuario>= 17 and tiene_suscripcion_premium == "si" and saldo_billetera >= Precio_suscripción)or(edad_usuario >= 17 and saldo_billetera >= Precio)
print("El usuario puede comprar el juego:", compra_exitosa)