import random
from copy import deepcopy
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

def pieza_aleatoria():
    i = random.randrange(len(piezas))
    return piezas[i]

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
