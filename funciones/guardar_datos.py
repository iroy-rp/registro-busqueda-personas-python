def datos(nombre, edad):
    with open("datos.txt", "a") as archivo:
        archivo.write(f"{nombre},{edad}\n")