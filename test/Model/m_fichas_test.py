import src.Model.m_fichas as fichas

# Si le damos una pieza erronea la función la reconoce i no la rotará.



def test_rotar_pieza_fail():
    pieza = [[1, 0],
             [1, 0],
             [1, 1]]
    assert(fichas.rotar_pieza(pieza) != False), "Pieza erronea detectada"

def test_rotar_pieza_pass():
    pieza = [[1, 1],
             [1, 0],
             [1, 1]]
    assert(fichas.rotar_pieza(pieza) != False), "Pieza erronea detectada"