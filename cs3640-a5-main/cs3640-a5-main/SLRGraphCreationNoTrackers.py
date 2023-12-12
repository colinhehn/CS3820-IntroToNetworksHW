import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load CSV data into a Pandas DataFrame
df = pd.read_csv('DataNoTrackerResults.csv')


# Correct column names
trackers_column = 'Number of Trackers'
loading_time_column = 'No Tracker Load Time'

# Plot the graph with correct data
plt.figure(figsize=(10, 6))
sns.regplot(x=trackers_column, y=loading_time_column, data=df, scatter_kws={'s':50})
plt.title('Number of Trackers vs. Loading Time when blocking trackers')
plt.xlabel('Number of Trackers')
plt.ylabel('Loading Time (seconds)')

# Calculate the correlation coefficient and p-val
correlation_coefficient, p_value = pearsonr(df[trackers_column], df[loading_time_column])

# Display the correlation coefficient, p-val, and sample size in the top right corner of the graph
plt.text(x=0.95, y=0.95, s=f'Correlation Coefficient: {correlation_coefficient:.2f}\nP-value: {p_value:.3e}\nSample Size: {len(df)}',
         horizontalalignment='right', verticalalignment='top', 
         transform=plt.gca().transAxes, fontsize=12)

plt.savefig('Graphs/NoTrackers.png')
plt.show()
