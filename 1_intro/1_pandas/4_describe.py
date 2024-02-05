import pandas as pd

base_credit = pd.read_csv('../../credit_risk_dataset.csv')

# Tenta descrever alguns padrões estatísticos da tabela
print(base_credit.describe())

#          person_age  ...  cb_person_cred_hist_length
# count  32581.000000  ...                32581.000000 # SOMATÓRIA
# mean      27.734600  ...                    5.804211 # MÉDIA
# std        6.348078  ...                    4.055001 # DESVIO PADRÃO
# min       20.000000  ...                    2.000000 # VALORES MÍNIMOS
# 25%       23.000000  ...                    3.000000
# 50%       26.000000  ...                    4.000000
# 75%       30.000000  ...                    8.000000
# max      144.000000  ...                   30.000000

