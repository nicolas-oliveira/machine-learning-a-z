import pandas as pd
import numpy as np

base_credit = pd.read_csv('../../wrong_data_credit_risk_dataset.csv')

# Separar colunas numéricas e não numéricas
# A razão de separar os dados numéricos e não numéricos é que algumas operações, como a função 'mean()',
# só podem ser aplicadas a dados numéricos (float64, int64 etc...) essa separação vai facilitar o processamento e
# permitir que preenchemos os dados incorretos com a 'média' ou 'o mais comum'.
numeric_columns = base_credit.select_dtypes(include=[np.number])
non_numeric_columns = base_credit.select_dtypes(exclude=[np.number])

# Calcular a média para colunas numéricas
mean_values = numeric_columns.mean()

# Encontre o valor mais usado para colunas não numéricas
most_common_values = non_numeric_columns.mode().iloc[0]

print("Valores médios para colunas numéricas:")
print(mean_values)

print("\nValores mais comuns para colunas não numéricas:")
print(most_common_values)
