import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
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
base_credit = pd.read_csv('../../credit_risk_dataset.csv')

grafico = px.scatter_matrix(base_credit, dimensions=['person_age', 'person_income', 'loan_amnt'], color = 'loan_status')

grafico.show()