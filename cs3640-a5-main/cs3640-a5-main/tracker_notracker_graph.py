import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv('DataNoTrackerResults.csv')
df2 = pd.read_csv('DataTrackerResults.csv')

# Merge the DataFrames based on the 'Website' column
merged_df = pd.merge(df1, df2, on='Website')

# Convert the website load time columns to float
merged_df['With Tracker Load Time'] = merged_df['With Tracker Load Time'].astype(float)
merged_df['No Tracker Load Time'] = merged_df['No Tracker Load Time'].astype(float)

# Compute the difference between the loading times
merged_df['Time Difference'] = merged_df['With Tracker Load Time'] - merged_df['No Tracker Load Time']

# Remove rows with missing 'Time Difference' values
merged_df = merged_df.dropna(subset=['Time Difference'])

# Compute the average difference
average_difference = merged_df['Time Difference'].mean()

# Compute the F-statistic and p-value of the difference
fvalue, pvalue = stats.f_oneway(merged_df['With Tracker Load Time'], merged_df['No Tracker Load Time'])
print(f"F-statistic and P-value: {fvalue, pvalue}")

# Print the number of rows in the 'Time Difference' column
row_count = len(merged_df['Time Difference'])
print(f"Number of rows in the 'Time Difference' column: {row_count}")
print(f"Average difference in loading times: {average_difference}")

# Create 2 plots displaying the differenc, one with outliers and one without.
loading_times = [merged_df['With Tracker Load Time'], merged_df['No Tracker Load Time']]
# Create first plot with outliers
fig = plt.figure(figsize=(14,6))
ax0 = fig.add_subplot(121)
# Set labels and title
plt.xlabel('(Load Time With Trackers - Load Time With Trackers Blocked)')
plt.ylabel('Difference in Load Time (seconds)')
plt.title('Load Time Difference With Outliers')
plt.text(x=0.95, y=0.95,
         s=f'Mean difference: {average_difference:.4f}\nF-statistic: {fvalue:.2f}\nP-value: {pvalue:.3e}\nSample Size: {len(merged_df)}',
         horizontalalignment='right', verticalalignment='top', 
         transform=plt.gca().transAxes, fontsize=12)
# Create second plot without outliers
ax0.boxplot(merged_df['Time Difference'])
ax1 = fig.add_subplot(122)
ax1.boxplot(merged_df['Time Difference'], showfliers=False)
# Set labels and title
plt.xlabel('(Load Time With Trackers - Load Time With Trackers Blocked)')
plt.ylabel('Difference in Load Time (seconds)')
plt.title('Load Time Difference Without Outliers')

plt.tight_layout()

# Save and show the plot
plt.savefig('Graphs/TimeDifferences.png')
plt.show()
