'''
Clase de Puntos para establecer puntuación máxima.
'''
class Punts:
    # Inicialización, si maximo negativo => transforma positivo
    def __init__(self, maximo):
        self.puntos = 0
        self.maximo = abs(maximo)

    def sumar_puntos(self, puntos):
        self.puntos += puntos
        return self.puntos

    # Función que comprueba si llega al maximo de puntos.
    def puntuacion_maxima(self):
        return True if self.puntos >= self.maximo else False

    def get_puntos(self):
        return self.puntos

    '''
    Función creada para realizar test de pairwise. 
    Seria utilizada para variar los puntos a sumar cuando se haga linea.
    '''
    def puntuacion_pairwise_testing(self, r1, r2, r3, p):
        if (r1 == 1 or r1 == 2) and (r2 == 1 or r2 == 2) and (r3 == 1 or r3 == 2):
            self.puntos += (p+r1*r2)-r3
        else:
            self.puntos += 20
        return self.puntos