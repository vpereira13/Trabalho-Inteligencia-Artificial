"""Arquivo da classe de texto
"""
import contador


class Texto:
    """Classe de texto

    Parameters
    ----------
    nome : string
        Nome do arquivo ou diretório+arquivo
    idioma : int
        Valor inteiro, 0 ou 1, que representa 0 - português
                                              1 - inglês

    Attributes
    ----------
    __nome : string
        Nome do arquivo ou diretório+arquivo
    __idioma : int
        Valor inteiro, 0 ou 1, que representa 0 - português
                                              1 - inglês
    __caracteristica : list
        Lista de caracteres e suas quantidades

    """
    def __init__(self, nome, idioma=None):
        self.__nome = nome
        self.__idioma = idioma
        self.__caracteristica = contador.contador(nome)

    # Getters
    def get_idioma(self):
        return self.__idioma

    def get_caracteristica(self):
        return self.__caracteristica
