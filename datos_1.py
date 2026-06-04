"""
Aprendiendo a usar CSV en Python
"""

nombre = ""
edad = 0

from funciones.guardar_datos import datos
from funciones.mostrar_datos import mostrar_datos
from funciones.promedio_edades import promedio_edad
from funciones.registros_totales import registro_tot
from funciones.edad_max import edad_maxi
from funciones.edad_min import edad_mini
from funciones.bscr_persona import buscar_personas

while nombre != "salir":
    nombre = input("Ingrese su nombre: o escriba 'salir' para terminar: ")
    if nombre != "salir":
        try: 
            edad = int(input("Ingrese su edad: "))
            if edad < 18 or edad >100:
               print("Edad no válida. Por favor, ingrese una edad entre 18 y 100.")
               continue # Para volver a pedir el nombre si la edad no es válida
            else:
                datos(nombre, edad)
        except ValueError:
            print("Edad no válida. Por favor, ingrese un número entero.")
        continue # Para volver a pedir el nombre si la edad no es un número entero
    #else:
    #   exit



respuesta = input ("¿Desea mostrar los datos ingresados? (s/n): ")
if respuesta.lower() == "s":
    print(registro_tot())
    mostrar_datos()
    promedio_edad()
    edad_maxi()
    edad_mini()

respuesta_busqueda = input("¿Desea buscar un nombre específico? (s/n): ")
if respuesta_busqueda.lower() == "s":
    nombre_buscar = input("Ingrese el nombre que desea buscar: ")
    buscar_personas(nombre_buscar) 