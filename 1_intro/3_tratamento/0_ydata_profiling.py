import pandas as pd
import ydata_profiling as ydp

base_credit = pd.read_csv('../../wrong_data_credit_risk_dataset.csv')

profile = ydp.ProfileReport(base_credit)
profile.to_file("wrong_data_credit_risk_dataset.html")
