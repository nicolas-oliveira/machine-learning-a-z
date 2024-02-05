import pandas as pd
import numpy as np

base_credit = pd.read_csv('../../credit_risk_dataset.csv')
print(
    np.unique(base_credit['loan_status'], return_counts=True)
)
# Sabendo que 'loan_status' representa os clientes que pagaram ou não os empréstimos
# o numpy organiza os valores possíveis e conta seu total de valores
# Dessa forma temos:
# 0:  Que pagaram os créditos: 25473
# 1: Que não pagaram os créditos: 7108
# (array([0, 1]), array([25473,  7108]))