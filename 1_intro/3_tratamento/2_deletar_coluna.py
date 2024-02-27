import pandas as pd

base_credit = pd.read_csv('../../credit_risk_dataset.csv')

print(base_credit[base_credit['person_age'] < 0])

# Supondo que os dados da idade estejam errados e a maioria dos dados está errada
# A melhor decisão é deletar a coluna inteira.

base_credit2 = base_credit.drop('person_age', axis=1)

print(base_credit2)