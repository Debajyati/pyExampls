import pandas as pd
import numpy as np

# Loading a CSV file into a Pandas DataFrame
dataframe = pd.read_csv("../dataset/data.csv")

# Creating a DataFrame from a NumPy array with custom row names
arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["Sandip","Prince","Faisal","Piyush","Daykon","Anish","Arnab","Swappy","Debashish","1729"],[0,-1,3,10,5,4,7,7,9,10]], dtype=object)
df = pd.DataFrame(arr)
print(df, end='\n') # without custom row names

df = pd.DataFrame(arr)
df = df.set_axis(['Sl no.','Name','Attack-Points'], axis='rows') # with custom row names
print(df, end='\n')

# Selecting rows from a DataFrame based on multiple conditions

'''Converting all rows into columns
   and columns into rows 
   with the transpose method'''
df = df.transpose()
selected_rows = df[(len(df['Name']) > 5) & (df['Attack-Points'] > 4)]
print(selected_rows, end='\n\n')

# Creating a DataFrame from a NumPy array with custom column names
dframe = pd.DataFrame(arr)
trans_df = dframe.transpose()
df_with_cols = trans_df.set_axis(['Sl no.','Name','Attack-Points'], axis='columns') 
print(df_with_cols, end='\n\n')

# Select the first 7 rows
selected_rows = pd.concat([df_with_cols.head(7)])

print("First 7 rows:\n")
# Display the selected rows
print(selected_rows, end='\n')

# Select the last 7 rows
selected_rows = pd.concat([df_with_cols.tail(7)])
print("\nLast 7 rows:")
# Display the selected rows
print(selected_rows, end='\n')

# Perform a NumPy operation (e.g., multiply Duration by 2) and create a new column
dataframe['Double_Duration'] = np.multiply(dataframe['Duration'], 2)
print("New Dataframe:\n")
# Display the DataFrame with the new column
print(dataframe)
