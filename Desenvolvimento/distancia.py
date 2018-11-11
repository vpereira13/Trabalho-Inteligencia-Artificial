""" Arquvio auxiliar com função de calcular a distância entre dois textos
"""
from math import sqrt
from math import fsum


def distancia(texto1, texto2):
    """Função auxiliar que calcula a distância euclidiana entre dois textos

    Parameters
    ----------
    texto1 : tipo Texto
        Primeiro texto a ser comparado
    texto2 : tipo Texto
        Segundo texto a ser comparado

    Returns
    -------
    float
        Retorna a distância euclidiana entre os dois textos
    """

    d1 = []
    d2 = []

    # Coleta as características de cada texto
    for i, j in texto1.get_caracteristica():
        d1.append(j)
    for i, j in texto2.get_caracteristica():
        d2.append(j)

    # Faz a diferença entre os valores
    d = [a - b for a, b in zip(d1, d2)]

    # Eleva ao quadrado
    d = [x ** 2 for x in d]

    # Soma e tira a raíz
    dist = fsum(d)
    dist = sqrt(dist)

    return dist
