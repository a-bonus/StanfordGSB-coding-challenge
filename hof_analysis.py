import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the 'HallOfFame.csv' file into a DataFrame. This file contains information about Hall of Fame inductees.
hall_of_fame_df = pd.read_csv('HallOfFame.csv')

# Filter the DataFrame to include only players who have been inducted into the Hall of Fame.
inducted_hof_df = hall_of_fame_df[hall_of_fame_df['inducted'] == 'Y']

# Load the 'Master.csv' file into a DataFrame. This file contains detailed player information.
df_master = pd.read_csv('Master.csv')

# Select only the 'playerID' and 'birthCountry' columns from df_master for further analysis.
df_selected = df_master[['playerID', 'birthCountry']]

# Merge the selected player information with the Hall of Fame data using 'playerID' as the key.
merged_df = df_selected.merge(inducted_hof_df, on="playerID")

# Create a new DataFrame containing 'playerID', 'birthCountry', and 'yearid' (year of induction).
new_df = merged_df[["playerID", "birthCountry", "yearid"]]

# Count the occurrences of each combination of 'birthCountry' and 'yearid' to understand induction trends.
group_count = new_df.groupby(['birthCountry', 'yearid']).size().reset_index(name='Count')

# Sort the DataFrame by 'yearid' and 'birthCountry' to prepare for visualization.
sorted_df = group_count.sort_values(by=['yearid', 'birthCountry'])

# To account for years without inductions, fill missing 'birthCountry' and 'yearid' combinations with 0.
all_combinations = pd.MultiIndex.from_product([sorted_df['birthCountry'].unique(), sorted_df['yearid'].unique()], names=['birthCountry', 'yearid'])
sorted_df_filled = sorted_df.set_index(['birthCountry', 'yearid']).reindex(all_combinations, fill_value=0).reset_index()

# Sort the filled DataFrame to ensure correct chronological order.
sorted_df_filled.sort_values(by=['yearid', 'birthCountry'], inplace=True)

# Calculate the cumulative sum for each country to analyze the trend over years.
sorted_df_filled['Cumulative_Sum'] = sorted_df_filled.groupby('birthCountry')['Count'].cumsum()

# Visualization setup
plt.figure(figsize=(12, 6))

# Define custom colors for each birthCountry for visual clarity and aesthetics.
country_palette = {
    "CAN": "#add8e6",  
    "Cuba": "#3498db",
    "D.R.": "#90ee90",
    "Germany": "#008000",
    "Netherlands": "#ffa500",
    "P.R.": "#e74c3c",
    "Panama": "#ffff00",
    "United Kingdom": "#ff4500",
    "USA": "#b19cd9",
    "Venezuela": "#6a5acd"
}

# Create the line plot with the cumulative sum data.
sns.lineplot(data=sorted_df_filled, x='yearid', y='Cumulative_Sum', hue='birthCountry', marker='', drawstyle='steps-post', linewidth=2, palette=country_palette)

# Setting the y-axis to logarithmic scale to better visualize disparities in scales.
plt.yscale('log') 
plt.title('Hall of Fame by Country Through The Years (Logarithmic Scale)')
plt.xlabel('Year')
plt.ylabel('Cumulative HOF (Log Scale)')

# Customize the legend to be outside the plot for better visibility.
plt.legend(title='Country', bbox_to_anchor=(1, 1))
plt.show()
