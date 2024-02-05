import pandas as pd
base_credit = pd.read_csv('../../credit_risk_dataset.csv')

# Demonsta os 10 últimas linhas da tabela
print(base_credit.tail(10))

#        person_age  ...  cb_person_cred_hist_length
# 32571          60  ...                          26
# 32572          52  ...                          22
# 32573          56  ...                          19
# 32574          52  ...                          19
# 32575          52  ...                          20
# 32576          57  ...                          30
# 32577          54  ...                          19
# 32578          65  ...                          28
# 32579          56  ...                          26
# 32580          66  ...                          30