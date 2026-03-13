# ### Ejercicio 4

# El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, con el fin de tener una idea sobre su vulnerabilidad. Diseñe un algoritmo que pida al usuario su edad y la clasifique según la etapa del ciclo de vida que le corresponda. Verifique que el usuario no ingrese valores menores a cero. Clasificación etaria de la población colombiana:

# - Infancia [0-6) años)
# - Niñez [6 - 12) años)
# - Adolescencia (12 - 20 años)
# - Juventud (20 - 25 años)
# - Adultez (25- 60 años)
# - Ancianidad / Vejez (60 años o más)

# Trata de escribir tu propia versión antes de revisar la solución.


edad = int(input("Ingrese su edad: "))
if edad <= 0:
        print("Error")
elif edad < 6:
    etapa = "Infancia"
elif edad < 12:
    etapa = "Niñez"
elif edad < 20:
    etapa = "Adolescencia"
elif edad < 25:
    etapa = "Juventud"
elif edad < 60:
    etapa = "Adultez"
else:
    etapa = "Ancianidad / Vejez"
print(f"Pertenece al grupo de {etapa}")