#  💡 **Ejercicio 3: Sistema de Becas**
# Una universidad otorga becas a los estudiantes si cumplen **alguna** de estas dos condiciones:
 
# - Tener un promedio mayor o igual a 9.0.
# - Estar en un nivel socioeconómico nivel 1 **Y** tener un promedio mayor a 8.0.
 
#  📤 **Acción en Bitácora:** Diseña la lógica en Python utilizando variables y operadores relacionales y lógicos. Sube tu análisis y código a la bitácora de tu repositorio explicando cómo funciona la evaluación de tu programa.

Promedio = float(input("Ingrese su promedio:"))
Estrato = float(input("Ingrese su nivel socieconómico:"))
A = (Promedio>= 9 or (Promedio > 8 and Estrato == 1)) 
print("Comprobando si se le otorgará una beca", A)