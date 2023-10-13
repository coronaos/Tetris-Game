def leerFichero():
    with open("/FX505G/UNIVERSIDAD/2023-2024/TQS/PRACTIQUES/Tetris-Game/historial.txt") as f:
        texto = f.readlines()
        f.close()
        return texto


def escribirFichero(nombre, puntuacion):
    f = open("/FX505G/UNIVERSIDAD/2023-2024/TQS/PRACTIQUES/Tetris-Game/historial.txt", "a+")
    f.write("\n"+puntuacion+" "+nombre)
    f.close()

def rankingFichero():
    puntos = leerFichero()
    ordenadoP = sorted(puntos, reverse=True)
    return ordenadoP[0:3]
