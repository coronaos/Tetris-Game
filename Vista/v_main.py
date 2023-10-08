from Model.m_tablero import Tablero

if __name__ == "__main__":
    tablero = Tablero(20, 10)
    piexa = [[1,0],
     [1,0],
     [1,1]]
    tablero.colocar_pieza(piexa, (0, 20))