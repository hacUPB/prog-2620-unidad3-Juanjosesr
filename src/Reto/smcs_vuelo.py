# Reto Unidad 3

# Aeronave de referencia: Boeing 737-800 (bimotor comercial)
# CONSTANTES INVESTIGADAS Y JUSTIFICADAS:
# - Consumo base: 3.5 kg/km
#     El Boeing 737-800 consume aprox. 2500 kg/h a una velocidad crucero
#     de ~720 km/h. Entonces: 2500 / 720 = 3.47 kg/km aprox 3.5 kg/km

# - Headwind (viento en contra): +20% de consumo
#     Segun datos de Boeing Flight Planning, un headwind de ~50 nudos
#     incrementa el consumo entre 15% y 25%. Se adopta 20%.

# - Tailwind (viento a favor): -12% de consumo
#     EUROCONTROL indica una reduccion entre 10% y 15%.
#     Se adopta 12% como valor diferenciado del headwind.

# - Combustible inicial: 10000 kg
# - Reserva legal minima: 1500 kg
#     Equivale a ~45 minutos de vuelo según normas OACI Anexo 2.

# FASE 1 - Tablas de análisis

# TABLA 1 - ENTRADAS
# | Variable            | Descripcion                          | Ejemplo   |
# | combustible_inicial | Combustible al despegar              | 10000 kg  |
# | reserva_legal       | Combustible minimo legal             | 1500 kg   |
# | num_tramos          | Cantidad de tramos en la ruta        | 5         |
# | distancia           | Distancia del tramo (ingresa piloto) | 350 km    |
# | opcion_viento       | Tipo de viento (ingresa piloto)      | 1, 2 o 3  |

# TABLA 2 - SALIDAS
# | Variable               | Descripcion                         | Ejemplo               |
# | consumo                | Combustible gastado en el tramo     | 1470 kg               |
# | combustible_proyectado | Combustible estimado tras el tramo  | 8530 kg               |
# | combustible_actual     | Combustible real tras el tramo      | 8530 kg               |
# | tipo_viento            | Viento traducido a texto            | "headwind"            |
# | Alerta critica         | Mensaje si se viola la reserva      | "ALERTA COMBUSTIBLE"  |
# | Informe final          | Resultado al terminar el vuelo      | "VUELO COMPLETADO"    |

# TABLA 3 - CONSTANTES Y VARIABLES DE CONTROL
# | Nombre               | Valor          | Funcion en el bucle                        |
# | combustible_inicial  | 10000 kg       | Valor de partida                           |
# | reserva_legal        | 1500 kg        | Limite que no se puede cruzar              |
# | num_tramos           | 5              | Define cuantas veces se repite el for      |
# | tramo                | 1 hasta 5      | Termina el bucle cuando llega a 5          |
# | vuelo_completado     | True / False   | Termina el bucle con break si es False     |
# | combustible_actual   | Cambia c/tramo | Guarda el combustible despues de cada paso |



# FASE 2 - Pseudocódigo

# INICIO
#
# CONSTANTES
#     combustible_inicial = 10000
#     reserva_legal = 1500
#     num_tramos = 5
#
# FUNCION calcular_consumo_tramo(distancia, viento)
#     consumo_base = distancia * 3.5
#     Si viento es "headwind":
#         consumo_final = consumo_base * 1.20
#     Si viento es "tailwind":
#         consumo_final = consumo_base * 0.88
#     Si viento es otro:
#         consumo_final = consumo_base
#     Retornar consumo_final
#
# PROGRAMA PRINCIPAL
#     combustible_actual = combustible_inicial
#     vuelo_completado = True
#
#     Mostrar informacion inicial del vuelo
#
#     REPETIR para cada tramo del 1 al 5:
#
#         Pedir distancia al usuario
#         Pedir tipo de viento al usuario (1, 2 o 3)
#         Traducir opcion a texto (headwind, tailwind, crosswind)
#
#         consumo = calcular_consumo_tramo(distancia, tipo_viento)
#         combustible_proyectado = combustible_actual - consumo
#
#         Si combustible_proyectado <= reserva_legal:
#             Mostrar alerta critica
#             vuelo_completado = False
#             DETENER bucle (break)
#
#         Si no hay emergencia:
#             combustible_actual = combustible_proyectado
#             Mostrar informacion del tramo
#
#     FIN REPETIR
#
#     Si vuelo_completado es True:
#         Mostrar "VUELO COMPLETADO EXITOSAMENTE"
#         Mostrar combustible final y margen sobre reserva
#     Si no:
#         Mostrar "VUELO ABORTADO - EMERGENCIA DE COMBUSTIBLE"
#         Mostrar combustible al momento de abortar
#
# FIN



# FASE 3/4 - Código fuente/ Implementación en python

def calcular_consumo_tramo(distancia, viento):
    # Calcula los kg de combustible consumidos en un tramo según el viento
    consumo_base = distancia * 3.5

    if viento == "headwind":
        # Viento en contra: aumenta el consumo un 20%
        consumo_final = consumo_base * 1.20
    elif viento == "tailwind":
        # Viento a favor: reduce el consumo un 12%
        consumo_final = consumo_base * 0.88
    else:
        # Viento cruzado o nulo: consumo base sin cambio
        consumo_final = consumo_base

    return consumo_final


combustible_inicial = 10000   # kg - combustible al despegar
reserva_legal = 1500          # kg - minimo que nunca se puede usar
num_tramos = 5                # cantidad de tramos en la ruta

print("SMCS - Sistema de Monitoreo de Combustible y Seguridad")
print("Boeing 737-800 | Bimotor Comercial")
print("Combustible inicial: ", combustible_inicial, "kg")
print("Reserva legal minima: ", reserva_legal, "kg")
print("Tramos en la ruta: ", num_tramos)


# Variable que guarda el combustible actual (cambia en cada tramo)
combustible_actual = combustible_inicial
 
# Variable que controla si el vuelo termino bien o fue terminado
vuelo_completado = True
 
# Bucle for: recorre los 5 tramos de la ruta
for tramo in range(1, 6):
    print("TRAMO", tramo, "de 5")
 
    # Entrada de datos del tramo
    distancia = float(input("Ingrese la distancia del tramo (km): "))
 
    print("Tipo de viento:")
    print("1. headwind  (viento en contra)")
    print("2. tailwind  (viento a favor)")
    print("3. crosswind (viento cruzado o nulo)")
    opcion_viento = input("Ingrese la opcion (1, 2 o 3): ")
    
    if opcion_viento == "1":
        tipo_viento = "headwind"
    elif opcion_viento == "2":
        tipo_viento = "tailwind"
    else:
        tipo_viento = "crosswind"
    
    consumo = calcular_consumo_tramo(distancia, tipo_viento)
    
    combustible_proyectado = combustible_actual - consumo
 
    if combustible_proyectado <= reserva_legal:
        print("ALERTA DE COMBUSTIBLE")
        print("Combustible proyectado:", combustible_proyectado, "kg")
        print("Esto viola la reserva legal de", reserva_legal, "kg")
        print("Ruta ABORTADA. Aterrizando en aeropuerto alterno")
        vuelo_completado = False
        break
 
    # Si no hay emergencia, actualizar valor de combustible
    combustible_actual = combustible_proyectado
 
    # Mostrar informacion del tramo
    print("Distancia volada: ", distancia, "km")
    print("Tipo de viento: ", tipo_viento)
    print("Combustible consumido: ", consumo, "kg")
    print("Combustible restante: ", combustible_actual, "kg")
 
# Informe final del vuelo
if vuelo_completado == True:
    print("  RESULTADO: VUELO COMPLETADO EXITOSAMENTE")
    print("  Combustible final: ", combustible_actual, "kg")
    print("  Margen sobre reserva: ", combustible_actual - reserva_legal, "kg")
else:
    print("  RESULTADO: VUELO ABORTADO - EMERGENCIA DE COMBUSTIBLE")
    print("  Combustible al abortar: ", combustible_actual, "kg")


# Reflexión de uso de IA

# El código fue planteado ayudado a elaborar con una IA a la hora de plantear y comprender el tema, hallar los valores de constantes a utilizar para empezar la elaboración del código, cómo resolver las dudas que tenía debido a que no sabía el uso de funciones (por ejemplo el uso de la implementación de nombrar funciones), y distintas maneras de poder desarrollar el mismo 