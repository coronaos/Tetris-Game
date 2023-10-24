from copy import deepcopy
class Tablero:

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[0 for x in range(self.filas)] for y in range(self.columnas)]

    # donde pieza sería una del array y posicion la fila y columna donde colocamos
    def colocar_pieza(self, pieza, posicion):
        curr_piece_x = len(pieza)
        curr_piece_y = len(pieza[0])
        for i in range(curr_piece_x):
            for j in range(curr_piece_y):
                if self.tablero[posicion[0]+i][posicion[1]+j] == 0:
                    if pieza[i][j] == 1:
                        self.tablero[posicion[0]+i][posicion[1]+j] = pieza[i][j]

    def borrar_pieza(self, pieza, posicion):
        curr_piece_x = len(pieza)
        curr_piece_y = len(pieza[0])
        for i in range(curr_piece_x):
            for j in range(curr_piece_y):
                if self.tablero[posicion[0] + i][posicion[1] + j] == 1:
                    # CHEQUEAR QUE NO SE VAYA DEL TABLERO.
                    if pieza[i][j] == 1:
                        self.tablero[posicion[0] + i][posicion[1] + j] = 0

    def mover_abajo(self, pieza, posicion):
        filas = posicion[0] + 1
        columnas = posicion[1]
        self.borrar_pieza(pieza, posicion)
        result = (self.overlap_check(pieza, [filas, columnas]))
        if result == True:
            self.colocar_pieza(pieza, posicion)
            return posicion
        elif result == [20,20]:
            self.colocar_pieza(pieza, [filas, columnas])
            return False
        elif result == [21,21]:
            self.colocar_pieza(pieza, posicion)
            return False
        elif result == False:
            #self.borrar_pieza(pieza, posicion)
            self.colocar_pieza(pieza, [filas, columnas])
            return [filas, columnas]

    def mover_derecha(self, pieza, posicion):
        filas = posicion[0]
        columnas = posicion[1] + 1
        self.borrar_pieza(pieza, posicion)
        if (self.overlap_check(pieza, [filas, columnas])):
            self.colocar_pieza(pieza, posicion)
            return posicion
        else:
            # self.borrar_pieza(pieza, posicion)
            self.colocar_pieza(pieza, [filas, columnas])
            return [filas, columnas]

    def mover_izquierda(self, pieza, posicion):
        filas = posicion[0]
        columnas = posicion[1] - 1
        self.borrar_pieza(pieza, posicion)
        if self.overlap_check(pieza, [filas, columnas]):
            self.colocar_pieza(pieza, posicion)
            return posicion
        else:
            # self.borrar_pieza(pieza, posicion)
            self.colocar_pieza(pieza, [filas, columnas])
            return [filas, columnas]

    def linea_completa(self):
        num_filas = 0
        for i in range(self.columnas):
                if all(self.tablero[i]):
                    self.linea_eliminada(i)
                    num_filas += 1
        return num_filas

    def linea_eliminada(self, fila):
        # eliminamos la fila que se ha completado
        del self.tablero[fila]
        # añadimos una fila de 0 en la parte superior (stack)
        self.tablero.insert(0, [0] * self.filas)

    def tablero_lleno(self, colocada):
        if colocada:
            for i in self.tablero[0:][0]:
                if i == 1:
                    return True
        return False

    def overlap_check(self, pieza, posicion):
        curr_piece_size_x = len(pieza)
        curr_piece_size_y = len(pieza[0])

        for i in range(curr_piece_size_x):
            for j in range(curr_piece_size_y):
                if (posicion[1] + j < self.filas) and  (posicion[1] + j > -1) and (posicion[0] + i < self.columnas):
                    # si no pasa las barreras del tablero
                    if (posicion[0] + i == self.columnas-1) and (self.tablero[self.columnas-1][posicion[1]+j] == 0):
                        # si llega al final del tablero y se coloca si o si
                        return [20, 20]
                    if (self.tablero[posicion[0] + i][posicion[1] + j] == 1) and (pieza[i][j] == 1):
                        # si en la pieza hay un 1 y en el tablero tambien(choque de piezas)
                        return [21, 21]
                else:
                    # si pasa las barreras del tablero
                    return True
        return False

