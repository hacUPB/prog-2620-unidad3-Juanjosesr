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
    opcion_viento = float(input("Ingrese la opcion (1, 2 o 3): "))
    
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
 
    # Si no hay emergencia, actualizar el valor de combustible
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
    3