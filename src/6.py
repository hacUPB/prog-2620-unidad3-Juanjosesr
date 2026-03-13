# ### Ejercicio 6

# Una compañía de paquetería internacional tiene servicio en algunos países según su zona. El costo por el servicio de paquetería se basa en el peso del paquete y la zona a la que va dirigido. Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados por seguridad. Usa la siguiente tabla para resolver el problema:

Peso = int(input("Ingrese el peso de su paquete: "))
Zona = int(input("Ingrese la zona a la que será llevado su paquete: "))


if Peso >= 5000:
    print("Su paquete no será transportador por seguridad")
else: 
    if Zona == 1:
           costo = Peso * 11
    elif Zona == 2:
        costo = Peso * 10
    elif Zona == 3:
        costo = Peso * 12
    elif Zona == 4:
        costo = Peso * 24
    elif Zona == 5:
        costo = Peso * 27
    else:
        costo = None

    if costo is not None:
        print(f"El costo del envío es: ${costo}")
    else:
        print("Ingrese una zona entre 1 y 5.")