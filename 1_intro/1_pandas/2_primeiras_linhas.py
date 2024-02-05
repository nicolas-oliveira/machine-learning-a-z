import pandas as pd
base_credit = pd.read_csv('../../credit_risk_dataset.csv')

# Demonstra os 10 primeiras linhas da tabela
print(base_credit.head(10))

#    person_age  ...  cb_person_cred_hist_length
# 0          22  ...                           3
# 1          21  ...                           2
# 2          25  ...                           3
# 3          23  ...                           2
# 4          24  ...                           4
# 5          21  ...                           2
# 6          26  ...                           3
# 7          24  ...                           4
# 8          24  ...                           2
# 9          21  ...                           3