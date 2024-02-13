import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

base_credit = pd.read_csv('../../credit_risk_dataset.csv')
sns.boxplot(y = base_credit['loan_grade'], x = base_credit['loan_amnt'])
plt.show()