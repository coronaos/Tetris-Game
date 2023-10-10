def leerFichero():
    with open('historial.txt') as f:
        texto = f.readlines()
        f.close()
        return texto


def escribirFichero(nombre, puntuacion):
    f = open('historial.txt', 'a+')
    f.write("\n"+puntuacion+" "+nombre)
    f.close()

def rankingFichero():
    puntos = leerFichero()
    ordenadoP = sorted(puntos, reverse=True)
    return ordenadoP[0:3]
