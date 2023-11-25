from src.Model.m_ficheros import Fichero
import os
import unittest

'''
Clase de test para comprobar funcionalidad ficheros. 
'''
class TestFichers(unittest.TestCase):

    '''
    Incialización de fichero
    IMPORTANTE: Diferente al de producción.
    '''
    def setUp(self):
        self.m_fichero_test = Fichero("\historial_test.txt")
        open(self.m_fichero_test.fichero, 'w').close()

    '''
    Función que elimina datos del fichero para realizar los casos de prueba.
    '''
    def deletePath(self):
        open(self.m_fichero_test.fichero, 'w').close()

    def test_escribirFichero(self): #Test para revisar que se escribe bien la puntuación y nombre en el historial
        usuario = "usuario1"
        puntuacion = 100
        self.m_fichero_test.escribirFichero(usuario, puntuacion)

        with open(self.m_fichero_test.fichero, 'r') as file:
            contents = file.read()
            self.assertIn(f"{puntuacion} {usuario[0:3]}", contents)

        self.deletePath()

    def test_leerFichero(self):
        self.m_fichero_test.escribirFichero("us1", 100)

        fichero_leido = self.m_fichero_test.leerFichero()
        for i in fichero_leido:
            self.assertIn(f"100 us1", i)

        self.deletePath()

    def test_rankingFichero(self):
        correct_answer = [100, 100, 50]
        self.m_fichero_test.escribirFichero("us1", 0)
        self.m_fichero_test.escribirFichero("us1", 100)
        self.m_fichero_test.escribirFichero("us1", 50)
        self.m_fichero_test.escribirFichero("us1", 20)
        self.m_fichero_test.escribirFichero("us1", 100)

        fichero_rank = self.m_fichero_test.rankingFichero()
        aux = 0

        for i in fichero_rank:
            self.assertIn(f"{correct_answer[aux]} us1", i)
            aux = aux + 1

        self.deletePath()