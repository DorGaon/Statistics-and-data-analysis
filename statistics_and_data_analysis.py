# -*- coding: utf-8 -*-
"""Statistics and data analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BH0xTSzhKr9OszCKcanfNVj04NgIbphz

ייבוא ספריות פייתון שיעזרו לנו לנתח את הנתונים:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import statsmodels.api as sm

df = pd.read_csv('onlinefoods.csv')

df.head()

df.drop(columns='Unnamed: 12', inplace=True)

df.head()

new_var = df.shape
new_var

df.describe()

df.head()

age_counts = df['Age'].value_counts().sort_index()

plt.bar(age_counts.index, age_counts.values, color='steelblue', edgecolor='black')
plt.title('Distribution of Ages', fontsize=16)
plt.xlabel('Ages', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tight_layout()
plt.show()

from scipy.stats import chi2_contingency

contingency_table = pd.crosstab(df['Marital Status'], df['Educational Qualifications'])

chi2, p, dof, expected = chi2_contingency(contingency_table)
average_income = round(df['Monthly Income'].mean(),2)

print("Chi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print('Average Monthly Income is: ', average_income)
print('Amount of observations, variables is : ',new_var)

df.describe()



df.loc[df['Monthly Income'] == '10001 to 25000', 'Monthly Income'] = 17500
df.loc[df['Monthly Income'] == '25001 to 50000', 'Monthly Income'] = 37500
df.loc[df['Monthly Income'] == 'Below Rs.10000', 'Monthly Income'] = 10000
df.loc[df['Monthly Income'] == 'More than 50000', 'Monthly Income'] = 50000
df.loc[df['Monthly Income'] == 'No Income', 'Monthly Income'] = 0

df.loc[df['Occupation'] == 'Employee', 'Occupation'] = 100
df.loc[df['Occupation'] == 'Self Employeed', 'Occupation'] = 100
df.loc[df['Occupation'] == 'Student', 'Occupation'] = 50
df.loc[df['Occupation'] == 'House wife', 'Occupation'] = 0

df.loc[df['Marital Status'] == 'Married', 'Marital Status'] = 2
df.loc[df['Marital Status'] == 'Single', 'Marital Status'] = 1
df.loc[df['Marital Status'] == 'Prefer not to say', 'Marital Status'] = 0

df.head()

df = df[[ 'Marital Status', 'Occupation', 'Age', 'Monthly Income']].dropna()
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Monthly Income'] = df['Monthly Income'].astype(str).str.strip()
df['Monthly Income'] = pd.to_numeric(df['Monthly Income'], errors='coerce')
df = df.dropna()

X = df['Age']
y = df['Monthly Income']

X = sm.add_constant(X)

model = sm.OLS(y, X)
result = model.fit()

print(result.summary())

df.head()

import statsmodels.api as sm

X = df_clean[['Marital Status', 'Occupation', 'Age']]
y = df_clean['Monthly Income']

X = sm.add_constant(X)

model = sm.OLS(y, X)
result = model.fit()

p_values = result.pvalues

print(result.summary())

print("P-values for each coefficient:")
print(p_values)

df['Monthly Income'] = df['Monthly Income'].astype(int)

plt.figure(figsize=(10, 6))
sns.histplot(df['Monthly Income'], bins=20, kde=True)
plt.title('Income Distribution')
plt.xlabel('Monthly Income')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='Monthly Income', y='Age', data=df)
plt.title('Age Distribution by Age')
plt.xlabel('Monthly Income')
plt.ylabel('Age')
plt.show()

sns.scatterplot(x='Age', y='Monthly Income', data=df)

# הוספת קו רגרסיה
sns.regplot(x='Age', y='Monthly Income', data=df, scatter=False, color='red')

plt.title('Monthly Income Distribution by Age')
plt.xlabel('Age')
plt.ylabel('Monthly Income')
plt.show()

pd.DataFrame(df.groupby('Marital Status')['Monthly Income'].mean().sort_values(ascending=False))

marital_status_counts = df['Marital Status'].value_counts()

plt.bar(marital_status_counts.index, marital_status_counts.values, color='grey')
plt.title('Marital Status Distribution', fontsize=20)
plt.xlabel('Marital Status', fontsize=16)
plt.ylabel('Count',fontsize=16)
plt.show()

income_pattern = df.groupby('Occupation')['Monthly Income'].mean()

plt.figure(figsize=(6,4))
plt.bar(income_pattern.index, income_pattern.values, color='lightpink', edgecolor='black')
plt.title('Income Patterns')
plt.xlabel('Occupation')
plt.ylabel('Income')
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()

df.head()

sns.countplot(x='Gender',data=df)
plt.show()

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

columns = ['Age', 'Monthly Income']

kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
kmeans.fit(df[columns])

labels = kmeans.labels_
df['Cluster'] = labels

cluster_counts = df['Cluster'].value_counts().sort_index()

plt.bar(cluster_counts.index, cluster_counts.values, color='#6495ED')
plt.xlabel('Cluster', fontsize=16)
plt.ylabel('Number of Members', fontsize=16)
plt.title('Number of Members in Each Cluster', fontsize=20)

plt.gca().patch.set_facecolor('#F0E68C')
plt.gcf().set_facecolor('#FBCEB1')

plt.show()