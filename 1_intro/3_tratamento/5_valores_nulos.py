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

base_credit.isnull()