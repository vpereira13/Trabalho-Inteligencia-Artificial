""" Funções auxiliares
"""


def contador(palavra):
    """Função que conta quantas vogais e quantas consoantes possuem em uma
       palavra

       Retorna uma tupla contendo o número de vogais e o número de
       consoantes da palavra
    """
    numero_vogais = 0
    numero_consoantes = 0
    palavra = palavra.lower()
    for letra in palavra:
        if letra in "aeiou":
            numero_vogais += 1
        else:
            numero_consoantes += 1
    return (numero_vogais, numero_consoantes)
