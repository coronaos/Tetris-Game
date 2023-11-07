import src.Model.m_fichas as fichas

# Si le damos una pieza erronea la función la reconoce i no la rotará.

def rotar_pieza_erronea(pieza):
    assert(fichas.rotar_pieza(pieza) != False), "Pieza erronea detectada"