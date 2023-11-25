import random
from copy import deepcopy

# Array de piezas disponibles
piezas = [

    [[1], [1], [1], [1]],

    [[1, 0],
     [1, 0],
     [1, 1]],

    [[0, 1],
     [0, 1],
     [1, 1]],

    [[0, 1],
     [1, 1],
     [1, 0]],

    [[1, 1],
     [1, 1]]
]

# Array de todos los diferentes estados de cada una de las piezas
piezas_completas = [
    [[1], [1], [1], [1]],

    [[1, 0],
     [1, 0],
     [1, 1]],

    [[0, 1],
     [0, 1],
     [1, 1]],

    [[0, 1],
     [1, 1],
     [1, 0]],

    [[1, 1],
     [1, 1]],

    [[1, 1, 1],
     [1, 0, 0]],

    [[1, 1],
     [0, 1],
     [0, 1]],

    [[0, 0, 1],
     [1, 1, 1]],

    [[1, 0, 0],
     [1, 1, 1]],

    [[1, 1],
     [1, 0],
     [1, 0]],

    [[1, 1, 1],
     [0, 0, 1]],

    [[1, 1, 0],
     [0, 1, 1]],

]

# Función que coge de forma aleatoria una pieza del array
def pieza_aleatoria():
    i = random.randrange(len(piezas))
    return piezas[i]

# Función que rota la pieza correspondiente
def rotar_pieza(pieza):
    if(pieza in piezas_completas):
        copiaPieza = deepcopy(pieza)
        reversa = copiaPieza[::-1]
        piezafinal = []
        for element in zip(*reversa):
            piezafinal.append(list(element))
        return piezafinal
    else:
        return False
