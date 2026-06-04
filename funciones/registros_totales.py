def registro_tot():
    contador =  0 
    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            contador += 1
    return(f"Total de registros: {contador}")