#💡 **Ejercicio 2: El guardián de la montaña rusa**
# Para subir a la nueva montaña rusa del parque, los visitantes deben medir al menos 150 cm.
# Escribe un programa donde declares una variable `altura_visitante` (asígnale el valor que quieras). Luego, utiliza un operador relacional para imprimir `True` si puede subir o `False` si no puede.
 
 
#📤 **Acción en Bitácora:** Escribe tu solución, pruébala con una altura de 145 y otra de 160. Sube tus hallazgos a la bitácora de tu repositorio.


Altura_visitante = float(input("Ingrese su altura (cm):"))

print("Comprobando si es mayor que 150")
A = Altura_visitante >= 150
print(A)

# se coloca solamente así xq al cumplirse el operador relacional y pedirle que lo imprima, nos da como respuesta colocar si es verdadero ("true") o falso ("false")
