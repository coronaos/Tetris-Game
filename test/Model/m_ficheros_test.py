from src.Model.m_ficheros import Fichero
import os
import unittest

script_dir = os.path.dirname(os.path.abspath(__file__))

nombre = "MATIES"
puntuacion = "200"
class TestFichers(unittest.TestCase):
    def setUp(self):
        self.m_fichero_test = Fichero("\historial_test.txt")
        open(self.m_fichero_test.fichero, 'w').close()
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
        
        self.m_fichero_test.escribirFichero("us2", 50)
        self.m_fichero_test.escribirFichero("us3", 20)

