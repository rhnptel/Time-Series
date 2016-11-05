import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as tsa


df = pd.read_csv('/Users/rohanpatel/Downloads/LoanStats3b.csv', header=1, low_memory=False)


#converts string to datetime
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

loan_count_summary.plot()
plt.show()

tsa.plot_acf(loan_count_summary)
plt.show()

tsa.plot_pacf(loan_count_summary)
plt.show()
