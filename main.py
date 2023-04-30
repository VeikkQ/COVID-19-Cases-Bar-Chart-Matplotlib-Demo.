import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Python\covid\WHO_COVID_19-global_table_data.csv')

df =df[['Name','Cases - cumulative total per 100000 population']]
df = df.set_index('Name')
fig, ax = plt.subplots(figsize=(16, 8), dpi=250)
plt.bar(df.index, df['Cases - cumulative total per 100000 population'])
plt.title('COVID-19 Cases per 100,000 Population by Country')
plt.xlabel('Country Names')
plt.ylabel('Cases per 100000 population')
plt.xticks(rotation=90, fontsize=4)
plt.subplots_adjust(bottom=0.3)
plt.show()