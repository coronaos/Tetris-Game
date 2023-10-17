def print_all(tablero, ficha):
    visual_ficha = print_ficha_siguiente(ficha)
    visual_tablero = print_tablero(tablero)
    for x, y in (visual_tablero, visual_ficha):
        print("\033[{0};{1}f{2}".format(2 + cont, 80, visual))
    for x in tablero:
        visual = []
        for y in x:
            if y == 0:
                visual.append("  ")
            elif y == 1:
                visual.append("[]")
        print(visual)
def print_ficha_siguiente(ficha_siguiente):
    cont = 0
    visual_ficha = []
    for x in ficha_siguiente:
        visual = []
        for y in x:
            if y == 0:
                visual.append("  ")
            elif y == 1:
                visual.append("[]")
        print("\033[{0};{1}f{2}".format(2+ cont, 80, visual))
        cont += 1
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