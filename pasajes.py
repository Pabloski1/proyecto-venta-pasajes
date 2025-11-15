pasaje = 0
total = 0
ciudad = ""
precios = [18000, 18500, 20580, 18600]
maleta_adicional = 5000
ventasciudad = {"Santiago": 0, "Arica": 0, "Temuco": 0, "Concepción": 0}
sent = True

while sent:
    print("*************PASAJE INTERURBANOS*****************\n"
        "¿Qué pasaje interurbano desea?\n"
        "1. Santiago - $18000\n"
        "2. Arica - $18500\n"
        "3. Temuco - $20580\n"
        "4. Concepción - $18600\n"
        "*************************************************\n")

    num = int(input("Ingrese el número a donde desea viajar: "))
    if 1 <= num <= 4:
        if num == 1:
            pasaje = precios[0]
            ciudad = "Santiago"
        elif num == 2:
            pasaje = precios[1]
            ciudad = "Arica"
        elif num == 3:
            pasaje = precios[2]
            ciudad = "Temuco"
        else:
            pasaje = precios[3]
            ciudad = "Concepción"

        respuesta = input("Desea pasaje de vuelta? Si/No: \n").upper()
        if respuesta == "SI":
            pasaje *= 2

        print("¿Cuánto equipaje lleva al viaje? (Si la cantidad excede 1 maleta, se le cobrará $5000 por maleta extra)")
        canMal = int(input("Cantidad de maletas: "))
        extraMal = 0

        if canMal > 1:
            extraMal = (canMal - 1) * maleta_adicional
            total += extraMal
        total += pasaje

        ventasciudad[ciudad] += 1

        print("\n*************PASAJE INTERURBANOS*****************")
        if respuesta == "SI":
            print("Destino:", ciudad, "ida y vuelta Valor $", pasaje)
        else:
            print("Destino:", ciudad, " ida Valor $", pasaje)
        print("Unidades de equipaje: ", canMal, " Valor $", extraMal)
        print("Total: $", total)
        print("\n****************************************************")

        nuevopasaje = input("¿Desea otro pasaje? Si/No: \n").upper()
        if nuevopasaje != "SI":
            sent = False
    else:
        print("El número ingresado es incorrecto. Inténtelo nuevamente.\n")

print("*************PASAJE INTERURBANOS*****************\n"
    "Resumen de ventas del día")
for ciudad, cantidad in ventasciudad.items():
    print(ciudad, cantidad)
print("TOTAL EN PASAJES: $", total, "\n"
    "TOTAL EN MALETAS: $", total, "\n"
    "*************************************************")

