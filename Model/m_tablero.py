from copy import deepcopy
class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        #self.tablero = [[0] * columnas for _ in range(filas)]
        self.tablero = [[0 for x in range(self.filas)] for y in range(self.columnas)]


    # donde pieza sería una del array y posicion la fila y columna donde colocamos
    def colocar_pieza(self, pieza, posicion):
        curr_piece_x = len(pieza)
        curr_piece_y = len(pieza[0])
        for i in range(curr_piece_x):
            for j in range(curr_piece_y):
                if (self.tablero[posicion[0]+i][posicion[1]+j] == 0):
                    self.tablero[posicion[0]+i][posicion[1]+j] = pieza[i][j]
    def borrar_pieza(self, pieza, posicion):
        curr_piece_x = len(pieza)
        curr_piece_y = len(pieza[0])
        for i in range(curr_piece_x):
            for j in range(curr_piece_y):
                if self.tablero[posicion[0] + i][posicion[1] + j] == 1:
                    # CHEQUEAR QUE NO SE VAYA DEL TABLERO.
                    self.tablero[posicion[0] + i][posicion[1] + j] = 0
    def mover_abajo(self, pieza, posicion):
        filas = posicion[0] + 1
        columnas = posicion[1]
        self.borrar_pieza(pieza, posicion)
        result = (self.overlap_check(pieza, [filas, columnas]))
        if result == True:
            self.colocar_pieza(pieza, posicion)

            return posicion
        elif(result == [20,20]):
            self.colocar_pieza(pieza, [filas, columnas])
            return False
        elif(result == [21,21]):
            self.colocar_pieza(pieza, posicion)
            return False
        else:
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
            #self.borrar_pieza(pieza, posicion)
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
            #self.borrar_pieza(pieza, posicion)
            self.colocar_pieza(pieza, [filas, columnas])
            return [filas, columnas]

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
                if (posicion[1] + j) < 10 and posicion[1] + j > -1 and (posicion[0] + i) < 20:
                    if (self.tablero[posicion[0] + i][posicion[1] + j] == 1 and pieza[i][j] == 1):
                        return[21,21]
                    elif(posicion[0] + i == 19):

                        return[20,20]
                else:

                    return True

        return False
    def print_tablero(self):
        """
        for i in range(self.filas -1,-1,-1):
            for j in range (self.columnas-1, -1, -1):
                print(self.tablero[i][j])

            print("\n")
        """

        for x in self.tablero:
            visual = []
            for y in x:
                if(y == 0):
                    visual.append("  ")
                elif(y == 1):
                    visual.append("[]")
            print(visual)