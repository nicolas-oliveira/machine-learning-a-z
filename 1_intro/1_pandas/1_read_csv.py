import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('../../credit_risk_dataset.csv')
print(base_credit)

# Colunas da base de dados

# person_age
# person_income
# person_home_ownership
# person_emp_length
# loan_intent
# loan_grade
# loan_amnt
# loan_int_rate
# loan_status
# loan_percent_income
# cb_person_default_on_file
# cb_person_cred_hist_length

#        person_age  ...  cb_person_cred_hist_length
# 0              22  ...                           3
# 1              21  ...                           2
# 2              25  ...                           3
# 3              23  ...                           2
# 4              24  ...                           4
# ...           ...  ...                         ...
# 32576          57  ...                          30
# 32577          54  ...                          19
# 32578          65  ...                          28
# 32579          56  ...                          26
# 32580          66  ...                          30
