# ejercicio 1

#Imagina que fuiste a cenar con 3 amigos (son 4 en total). La cuenta fue de $85. Además, quieren dejar un 15% de propina. 
# Escribe un programa en Python que calcule:
# 1. El total de la propina.
# 2. El total a pagar (cuenta + propina).
# 3. Cuánto debe pagar cada uno, dividiendo en partes iguales.

# 📤 **Acción en Bitácora:** Crea un archivo llamado `ejercicio1_aritmetica.py`, resuelve el problema y sube el código junto con una captura de pantalla de la ejecución a la bitácora de tu repositorio.

Cuenta = float(85)
propina = float(0.15)

Total_propina = Cuenta * propina
Total_pagar = Cuenta + Total_propina
Total_persona = Total_pagar / 4
print("El total de la propina es: $", Total_propina)
print("El total a pagar es: $", Total_pagar)
print("El total a pagar por persona es: $", Total_persona)