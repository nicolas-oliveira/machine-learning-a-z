# Antes de entender os métodos que auxiliam a manipular dados tanto corrigindo
# Quanto deletando ou manipulando devemos entender a diferença entre média e mediana
# Utilizando as duas bibliotecas numpy e pandas é possível obter os dois.
import numpy as np
import pandas as pd


def printa_dados(media, mediana):
    print("------")
    print("Média:", media)
    print("Mediana:", mediana)
    print("------")


conjunto = [4, 3, 1, 6, 1, 7]

dados = np.array(conjunto)
dados2 = pd.Series(conjunto)

# Média representa todos os elementos divididos pelo quantidade total de elementos
# Mediana representa o meio do caminho ao ordenar todos os elementos

# Calculando a média
media = np.mean(dados)
media2 = dados2.mean()

# Calculando a mediana
mediana = np.median(dados)
mediana2 = dados2.median()

print("\nNumpy:")
printa_dados(media, mediana)
print("\nPandas:")
printa_dados(media2, mediana2)

# -----------------------

conjunto2 = [0, 7, 50, 1000, 1000000]

dados3 = pd.Series(conjunto2)

media3 = dados3.mean()
mediana3 = dados3.median()

print("\nExtra:")
printa_dados(media3, mediana3)