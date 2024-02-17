import pandas as pd
import numpy as np

# Create a DataFrame from a complex dictionary of integer lists where the values range very different

data = {
    'A': [1, 2, 3, 4, 59],
    'B': [101, 20, 30, 69, 50],
    'C': [900, 200, 305, 479, 500],
    'D': [1000, 2000, 3000, 4096, 5089],
}

df = pd.DataFrame.from_dict(data) # craeting dataframe from dictionary

# Evaluate the correlation matrix
correlation_matrix = df.corr()
print("Correlation Matrix:\n", correlation_matrix, end='\n\n')

# Create a sample DataFrame using random integeral values
df = pd.DataFrame({
    'A': np.random.randint(0, 100, 100),
    'B': np.random.randint(0, 100, 100),
    'C': np.random.randint(0, 100, 100),
    'D': np.random.randint(0, 100, 100),
    'Frequency': np.random.randint(50, 525, 100),
})

# Create a NumPy array from the 'Values' column
numpy_array = np.array(df['Frequency'])

# Calculate the cumulative sum and store in a new column 'Cumulative_Sum'
df['Cumulative_Sum'] = np.cumsum(numpy_array)

# Display the DataFrame
print(df, end='\n\n')
