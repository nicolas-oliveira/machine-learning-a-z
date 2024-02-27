import pandas as pd

import plotly.express as px
import matplotlib.pyplot as plt



base_credit = pd.read_csv('../../credit_risk_dataset.csv')
px.scatter_matrix(base_credit, dimensions=[''])
plt.show()