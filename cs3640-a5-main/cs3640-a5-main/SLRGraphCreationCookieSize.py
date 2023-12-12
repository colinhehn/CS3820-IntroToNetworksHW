import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load CSV data into a Pandas DataFrame
df = pd.read_csv('DataMergedCookiesAndTrackers.csv')


# Create x and y variables
x_axis_column = 'Total bytes used by cookies'
y_axis_column = 'With Tracker Load Time'

# Plot the graph with correct data
plt.figure(figsize=(10, 6))
sns.regplot(x=x_axis_column, y=y_axis_column, data=df, scatter_kws={'s':50})
plt.title('Total bytes used by cookies vs. Loading Time when not blocking trackers')
plt.xlabel('Total bytes used by cookies')
plt.ylabel('Loading Time (seconds)')

# Calculate the correlation coefficient and the p-value
correlation_coefficient, p_value = pearsonr(df[x_axis_column], df[y_axis_column])

# Display the correlation coefficient, p-value, and sample size in the top right corner of the graph
plt.text(x=0.95, y=0.95, s=f'Correlation Coefficient: {correlation_coefficient:.2f}\nP-value: {p_value:.3e}\nSample Size: {len(df)}',
         horizontalalignment='right', verticalalignment='top', 
         transform=plt.gca().transAxes, fontsize=12)

plt.savefig('Graphs/CookieSize.png')
plt.show()