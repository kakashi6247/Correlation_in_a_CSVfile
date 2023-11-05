import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the path to your CSV file
csv_file = 'your_file.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Function to filter data based on conditions
def filter_data(df, condition):
    filtered_df = df[condition]
    return filtered_df

# Function to test correlation between two columns
def test_correlation(df, column1, column2):
    correlation = df[column1].corr(df[column2])
    return correlation

# User-defined conditions
condition = (df['Open'] < df['Close'])
#condition2 = (df['DatapointX'] > 2)

# Combine conditions using logical operators

# combined_condition = condition1 & condition2  
# You can use '&' (and) or '|' (or)

# Filter data based on the condition
filtered_data = filter_data(df, condition)

# Test correlation between DatapointX and DatapointY
correlation = test_correlation(filtered_data, 'High', 'Low')

# Print the filtered data and correlation result
print("Filtered Data:")
print(filtered_data)
print(f"Correlation between DatapointX and DatapointY: {correlation}")

# You can also create a scatter plot to visualize the data and correlation
plt.scatter(filtered_data['High'], filtered_data['Low'])
plt.xlabel('High')
plt.ylabel('Low')
plt.title(f"Scatter Plot - Correlation: {correlation}")
plt.show()