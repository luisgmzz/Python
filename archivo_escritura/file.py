from os import getcwd
import statistics


def mean(list):
    if len(list) == 0:
        return 0
    return statistics.mean(list)


class File:
    ruta_menores = f"{getcwd()}/datos/futbol-menores.txt"
    ruta_estadisticas = f"{getcwd()}/datos/estadisticas.txt"

    def __init__(self, file):
        self.file = file

    def ingresar(self, valores):
        cadena_final = f"{','.join(valores)}\n"

        self.file.write(cadena_final)
        return cadena_final

    def listar_menores(self):
        lineas = self.file.readlines()
        menores = list(filter(lambda x:  int(
            x[-3:-1]) < 18 and x.split(",")[4] == "futbol", lineas))
        with open(self.ruta_menores, "w") as f:
            for i in menores:
                f.write(i)

    def generar_estadisticas(self):
        lineas = self.file.readlines()
        deportes = {"futbol": [], "basquetbol": [], "tenis": []}
        for i in lineas:
            deportes[i.split(",")[4]].append(i)

        edades = {"futbol": [], "basquetbol": [], "tenis": []}
        sexos = {"futbol": {"h": 0, "m": 0}, "basquetbol": {
            "h": 0, "m": 0}, "tenis": {"h": 0, "m": 0}}

        for i in deportes.keys():
            for j in deportes[i]:
                edades[i].append(int(j[:-1].split(",")[5]))
                sexos[i][j.split(",")[3]] += 1
            edades[i] = mean(edades[i])

        with open(self.ruta_estadisticas, "w") as f:
            new_text = (f"futbol-> Promedio Edad: {edades['futbol']} | Hombres-Mujeres: {sexos['futbol']['h']}-{sexos['futbol']['m']}\n"
                        f"basquetbol-> Promedio Edad: {edades['basquetbol']} | Hombres-Mujeres: {sexos['basquetbol']['h']}-{sexos['basquetbol']['m']}\n"
                        f"tenis-> Promedio Edad: {edades['tenis']} | Hombres-Mujeres: {sexos['tenis']['h']}-{sexos['tenis']['m']}")
            f.write(new_text)
            return new_text
