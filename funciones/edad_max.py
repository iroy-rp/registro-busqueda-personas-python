def edad_maxi():
    edad_maxima = 0
    contador = 0

    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            nombre, edad = linea.strip().split(",")
            if int(edad) > edad_maxima:
                edad_maxima = int(edad)
            contador += 1
    if contador > 0:
        print(f"Edad máxima: {edad_maxima}")
    else:
        print("No hay datos disponibles.")