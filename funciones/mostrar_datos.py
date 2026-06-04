def mostrar_datos():
    contador = 0
    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            contador += 1
    if contador > 0:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                nombre, edad = linea.strip().split(",")
                print(f"Nombre: {nombre} - Edad: {edad}")
    else:
        print("No hay datos disponibles.")