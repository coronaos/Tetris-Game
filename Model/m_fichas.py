import random
piezas = [

    [[1], [1], [1], [1]],

    [[1,0],
     [1,0],
     [1,1]],

    [[0,1],
     [0,1],
     [1,1]],

    [[0,1],
     [1,1],
     [1,0]],

    [[1,1],
     [1,1]]
]

def pieza_aleatoria():
    i = random.randrange(len(piezas))
    return piezas[i]

print(pieza_aleatoria())