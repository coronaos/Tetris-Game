def print_all(tablero, ficha):
    visual_ficha = print_ficha_siguiente(ficha)
    visual_tablero = print_tablero(tablero)
    for fila1, fila2 in zip(visual_tablero, visual_ficha):
        fila_tablero = []
        fila_ficha = []
        for elem1 in fila1:
            fila_tablero.append(elem1)
        for elem2 in fila2:
            fila_ficha.append(elem2)
        print(f"{fila_tablero}    |    {fila_ficha}")
    for fila3 in visual_tablero[len(visual_ficha):]:
        aux = []
        for elem3 in fila3:
            aux.append(elem3)
        print(f"{aux}    |    ")
def print_ficha_siguiente(ficha_siguiente):
    visual_ficha = []
    for x in ficha_siguiente:
        visual = []
        for y in x:
            if y == 0:
                visual.append("  ")
            elif y == 1:
                visual.append("[]")
        visual_ficha.append(visual)
    return visual_ficha
def print_tablero(tablero):
    visual_tablero = []
    for x in tablero:
        visual = []
        for y in x:
            if y == 0:
                visual.append("  ")
            elif y == 1:
                visual.append("[]")
        visual_tablero.append(visual)
    return visual_tablero