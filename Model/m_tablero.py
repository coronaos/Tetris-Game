class Tablero:
    def __init__(self,filas,columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[0] * columnas for _ in range(filas)]

    def colocar_pieza(self,pieza,posicion):
        #no se muy bien como hacerlo
        pass

    def linea_completa (self, fila):
        #si toda la fila es diferente de 0 devuelve TRUE
        return all(self.tablero[fila])

    def linea_eliminada (self, fila):
        #eliminamos la fila que se ha completado
        del self.tablero[fila]
        #añadimos una fila de 0 en la parte superior (stack)
        self.tablero.insert(0,[0] * self.columnas)
