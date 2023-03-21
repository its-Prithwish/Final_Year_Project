import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# References:
# Using seaborn to plot bar graph: https://stackabuse.com/seaborn-bar-plot-tutorial-and-examples/

# Getting the data
data_set = pd.read_csv('Dataset.csv')
df_age = data_set['Age of Casualty']

# Created bins for age data
max_age = pd.DataFrame.max(df_age)
bins = np.arange(0, max_age+10, 10)

# Get data for each bin
age_bins = pd.cut(x=df_age, bins=bins)

# Plotting of bar graph
sns.set(font_scale=0.8)
values = age_bins.value_counts(sort=False).keys().tolist()
count = age_bins.value_counts(sort=False).tolist()
sns.barplot(x=values, y=count)

plt.xlabel("Accidents in age group", labelpad=8)
plt.ylabel("Total accident count", labelpad=8)
plt.title("Accidents count by age group", y=1)
plt.show()
