"""Função principal da simulação do ML
"""

import distancia
import texto

BASEBR = ['textos/texto-ptbr0',
          'textos/texto-ptbr1',
          'textos/texto-ptbr2',
          'textos/texto-ptbr3',
          'textos/texto-ptbr4',
          'textos/texto-ptbr5',
          'textos/texto-ptbr6',
          'textos/texto-ptbr7',
          'textos/texto-ptbr8',
          'textos/texto-ptbr9'
          ]
BASEEN = ['textos/texto-en0',
          'textos/texto-en1',
          'textos/texto-en2',
          'textos/texto-en3',
          'textos/texto-en4',
          'textos/texto-en5',
          'textos/texto-en6',
          'textos/texto-en7',
          'textos/texto-en8'
          ]

ALVO = 'textos/texto-en9'

if __name__ == '__main__':
    base_conhecimento = []

    # Preenchendo a base de conhecimento com textos e com os idiomas deles
    for arquivo in BASEBR:
        t = texto.Texto(arquivo, 0)
        base_conhecimento.append(t)
    for arquivo in BASEEN:
        t = texto.Texto(arquivo, 1)
        base_conhecimento.append(t)

    # Iniciando um novo texto, não conhecido
    novo = texto.Texto(ALVO)

    # Calcula as distancias entre o novo e os arquivos da base de conhecimento
    distancias = []
    for t in base_conhecimento:
        distancias.append((distancia.distancia(novo, t), t.get_idioma()))

    # Distancia entre a entrada e os dados da base
    distancias.sort()

    resultado = 0

    # Aplica algoritmo dos k-NN (no caso 5)
    for i in distancias[:3]:
        resultado += i[1]
    resultado /= 3

    # Saída do resultado
    if int(resultado):
        print("Texto inserido em inglês")
    else:
        print("Texto inserido em português")
