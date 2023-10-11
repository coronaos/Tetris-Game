def leerFichero():
    with open("/Users/matieslopezalarcon/Documents/GitHub/Tetris-Game/Model/historial.txt") as f:
        texto = f.readlines()
        f.close()
        return texto


def escribirFichero(nombre, puntuacion):
    f = open("/Users/matieslopezalarcon/Documents/GitHub/Tetris-Game/Model/historial.txt", "a+")
    f.write("\n"+puntuacion+" "+nombre)
    f.close()

def rankingFichero():
    puntos = leerFichero()
    ordenadoP = sorted(puntos, reverse=True)
    return ordenadoP[0:3]
