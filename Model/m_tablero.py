class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[0] * columnas for _ in range(filas)]

    # donde pieza sería una del array y posicion la fila y columna donde colocamos
    def colocar_pieza(self, pieza, posicion):
        if posicion[0] >= self.filas or posicion[0] < 0:
            exit("La fila no que corresponde al tamaño")
        if posicion[1] >= self.columnas or posicion[1] < 0:
            exit("La columna no que corresponde al tamaño")
        for i, fila in enumerate(pieza):
            for j,cell in enumerate(fila):
                if cell:
                    #CHEQUEAR QUE NO SE VAYA DEL TABLERO.
                    self.tablero[posicion[0] + i][posicion[1] + j] = cell

    def mover_abajo(self, pieza, posicion):
        filas = posicion[0] - 1
        columnas = posicion[1]

        if self.overlap_check(pieza, posicion):
            print("No se puede mover abajo")
            return posicion
        else:
            self.colocar_pieza(pieza, (filas, columnas))
            return filas, columnas

    def mover_derecha(self, pieza, posicion):
        filas = posicion[0]
        columnas = posicion[1] + 1
        if self.overlap_check(pieza, posicion):
            print("No se puede mover a la derecha")
            return posicion
        else:
            self.colocar_pieza(pieza, (filas, columnas))
            return filas, columnas

    def mover_izquierda(self, pieza, posicion):
        filas = posicion[0]
        columnas = posicion[1] -1
        if self.overlap_check(pieza, posicion):
            print("No se puede mover a la izquierda")
            return posicion
        else:
            self.colocar_pieza(pieza, (filas, columnas))
            return filas, columnas

    def linea_completa(self):
        num_filas = 0
        for i in range(self.filas - 1, -1, -1):
                if all(self.tablero[i]):
                    self.linea_eliminada(i)
                    num_filas += 1
        return num_filas


    def linea_eliminada(self, fila):
        # eliminamos la fila que se ha completado
        del self.tablero[fila]
        # añadimos una fila de 0 en la parte superior (stack)
        self.tablero.insert(0, [0] * self.columnas)

    def tablero_lleno(self, pieza, posicion):
        if self.overlap_check(pieza, posicion) and posicion[0] == (self.filas-1):
            return True
        else:
            return False

    def overlap_check(self, pieza, posicion):
        curr_piece_size_x = len(pieza)
        curr_piece_size_y = len(pieza[0])
        for i in range(curr_piece_size_x):
            for j in range(curr_piece_size_y):
                if self.tablero[posicion[0] + i][posicion[1] + j] == 1 and pieza[i][j] == 1:
                    return False
        return True
    def print_tablero(self):
        for i in range(self.filas -1,-1,-1):
            for j in range (self.columnas-1, -1, -1):
                print(self.tablero[i][j])
            print("\n")


