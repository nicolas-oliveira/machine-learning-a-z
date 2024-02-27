# Quanto mais dados melhor para que a inteligência artificial aprenda.
# Se deletarmos todos os dados que estão incorretos, podemos ter um modelo mais burro
# portanto a indicação aqui é preencher com a média ou os valores mais comuns
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('../../wrong_data_credit_risk_dataset.csv')

# Média geral, incluindo os valores incorretos
print(base_credit['person_age'].mean())

# Média que exclui os valores incorretos
print(base_credit['person_age'][base_credit['person_age'] > 0].mean())

# Base de dados com erros
print(base_credit[base_credit['person_age'] < 0])

# Fazendo a substituição dos dados incorretos pela média dos valores

# ERRADO
# base_credit.loc[base_credit['person_age'] < 0] = 27.82
# print(base_credit.loc[5])

# CORRETO
base_credit.loc[base_credit['person_age'] < 0, 'person_age'] = 27.82
print(base_credit.loc[5])

# Base de dados corrigida
print(base_credit[base_credit['person_age'] < 0])