from file import File
from os import getcwd

RUTA_SOCIOS = f"{getcwd()}/datos/socios.txt"
operacion = input(("¿Que operación deseas hacer?\n"
                   "1-Ingresar un nuevo socio\n"
                   "2-Crear un archivo con los socios menores de edad que hacen futbol\n"
                   "3-Crear un archivo de estadisticas con la media de edades y el numero de hombres/mujeres por cada deporte\n"
                   "4-Salir\n"))

if operacion != "4":
    if operacion == "1":
        print("Introduce los datos sin comas\n")
        rut = input("Introduce el rut\n")
        apellido = input("Introduce el apellido\n").lower()
        nombre = input("Introduce el nombre\n").lower()
        genero = input("Introduce el genero (h/m)\n").lower()
        deporte = input(
            "Introduce el deporte (futbol/basquetbol/tenis)\n").lower()
        edad = input("Introduce la edad\n")
        if not edad.isdecimal() or genero not in ["h", "m"] or deporte not in ["futbol", "basquetbol", "tenis"] or "," in rut+apellido+nombre+edad:
            print("Introduce los datos correctamente!")
        else:
            with open(RUTA_SOCIOS, "a") as f:
                file = File(f)
                valores = [rut, apellido, nombre, genero, deporte, edad]
                resultado = file.ingresar(valores)
                print(f"Valores ingresados: {resultado}")
    elif operacion == "2":
        with open(RUTA_SOCIOS, "r+") as f:
            file = File(f)
            file.listar_menores()
        print("Menores listados!")
    elif operacion == "3":
        with open(RUTA_SOCIOS, "r+") as f:
            file = File(f)
            file.generar_estadisticas()
        print("Estadisticas generadas!")
else:
    print("Adiós\n")
