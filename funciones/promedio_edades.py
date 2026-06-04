def promedio_edad():
    total_edad = 0
    contador = 0
    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            nombre, edad = linea.strip().split(",")
            total_edad += int(edad)
            contador += 1
    if contador > 0:
        promedio = total_edad / contador
        print(f"Promedio de edad: {promedio}")
    else:
        print("No hay datos disponibles.")