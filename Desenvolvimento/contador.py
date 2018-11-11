'''Responsável por fazer a contagem de ocorrência de cada caracter do texto
'''
from collections import defaultdict
import string


PONTUACOES_BRANCOS = string.punctuation
PONTUACOES_BRANCOS += string.whitespace
ALFABETO = "qwertyuiopasdfghjklzxcvbnmáéíóúçüâêãõ"


def contador(filename):
    """Função que coleta as características os textos

    Parameters
    ----------
    filename : string
        Nome do arquivo a ser aberto para coletar informações

    Returns
    -------
    list
        Lista contendo o caracter e a sua respectiva quantidade presente no
        texto
    """

    count = defaultdict(int)
    for i in ALFABETO:
        count[i] = 0
    with open(filename, 'r') as arquivo:
        for linha in arquivo:
            for letra in linha:
                if letra not in PONTUACOES_BRANCOS:
                    count[letra.lower()] += 1
    count = sorted(count.items())

    return count


def imprime_frequencias(lista):
    """Função para debug, verificar os valores de cada caracter

    Parameters
    ----------
    lista : list
        Lista contendo os caracteres e as suas quantidades
    """

    for i in lista:
        print("{}, {}".format(i[0], i[1]))
