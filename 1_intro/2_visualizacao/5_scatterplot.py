import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

base_credit = pd.read_csv('../../credit_risk_dataset.csv')
sns.scatterplot(x = base_credit['loan_amnt'], y = base_credit['person_age'])
plt.show()