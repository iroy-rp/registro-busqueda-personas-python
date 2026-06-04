def buscar_personas(n_buscado):
    
    #n_buscado = input("Ingrese el nombre de la persona que desea buscar: ")

    encontrado = False

    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            nombre, edad = linea.strip().split(",")

            if n_buscado.lower() == nombre.lower():
                print(f"Nombre: {nombre}, Edad: {edad}")
                encontrado = True

    if  not encontrado:
        print("Persona no encontrada.")