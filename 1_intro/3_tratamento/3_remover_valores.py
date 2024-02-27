import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('../../wrong_data_credit_risk_dataset.csv')

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

wrong_values = base_credit[base_credit['person_age'] < 0]

# Supondo que alguns dos dados da idade estejam errados e a maioria dos dados está certa.
# A melhor decisão é remover os dados errados

print(wrong_values)
base_credit2 = base_credit.drop(wrong_values.index) # Deve-se indicar os índice da linha

print(base_credit2)