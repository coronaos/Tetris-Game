class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[0] * columnas for _ in range(filas)]

    # donde pieza sería una del array y posicion la fila y columna donde colocamos
    def colocar_pieza(self, pieza, posicion):
        if posicion[0] > self.filas or posicion[0] < 0:
            exit("La fila no que corresponde al tamaño")
        if posicion[1] > self.columnas or posicion[1] < 0:
            exit("La columna no que corresponde al tamaño")
        for i, fila in enumerate(pieza):
            for j,cell in enumerate(fila):
                if cell:
                    self.tablero[posicion[0] + i][posicion[1] + j] = cell

    def linea_completa(self, fila):
        # si toda la fila es diferente de 0 devuelve TRUE
        return all(self.tablero[fila])

    def linea_eliminada(self, fila):
        # eliminamos la fila que se ha completado
        del self.tablero[fila]
        # añadimos una fila de 0 en la parte superior (stack)
        self.tablero.insert(0, [0] * self.columnas)
