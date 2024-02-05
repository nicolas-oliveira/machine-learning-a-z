import pandas as pd

# Seleciona várias colunas e personaliza o resultado
columns = ["person_age", "person_income", "person_home_ownership",
           "loan_amnt", "loan_status"]
base_credit = pd.read_csv('../../credit_risk_dataset.csv', usecols=columns)
print(base_credit.describe())