def edad_mini():
    edad_min = 0
    contador = 0

    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            nombre, edad = linea.strip().split(",")
            if int(edad) < edad_min or edad_min == 0:
                edad_min = int(edad)
            contador += 1
    if contador > 0:
        print(f"Edad minima: {edad_min}")
    else:
        print("No hay datos disponibles.")