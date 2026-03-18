# ## 9. Ejercicio Propuesto

# **Menú Repetitivo**

# 1. Crea un menú de opciones (por ejemplo, 1: "Sumar", 2: "Restar", 3: "Salir").
# 2. Utiliza `while True:` para **mantener** el menú **hasta** que el usuario elija "Salir".
# 3. Emplea `match-case` (o `if-elif-else` si no tienes Python 3.10+) para gestionar cada opción.

# **ℹ️ Pregunta de Control**

# - ¿Cómo harías para terminar el bucle cuando el usuario elija "Salir"?
# - ¿En qué momento leerías la opción de usuario de nuevo para que el menú aparezca repetidamente?





# while True:
#     print("=== MENÚ ===")
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Salir")

#     opcion = input("Elige una opción: ")

#     if opcion == "1":
#         a = int(input("Número 1: "))
#         b = int(input("Número 2: "))
#         print(f"Resultado: {a + b}")
#     elif opcion == "2":
#         a = int(input("Número 1: "))
#         b = int(input("Número 2: "))
#         print(f"Resultado: {a - b}")
#     elif opcion == "3":
#         print("Ya")
#     else:
#         print("Error")


while True:
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            a = int(input("Número 1: "))
            b = int(input("Número 2: "))
            print(f"Resultado: {a + b}")
        case "2":
            a = int(input("Número 1: "))
            b = int(input("Número 2: "))
            print(f"Resultado: {a - b}")
        case "3":
            print("Ya")
        case _:
            print("Error")