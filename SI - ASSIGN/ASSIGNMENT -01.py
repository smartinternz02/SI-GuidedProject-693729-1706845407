import pandas as pd
import numpy as np

# Task 1: Create a pandas dataframe with numpy random values
np.random.seed(0)  # for reproducibility
data = np.random.randn(4, 4)  # 4 features and 4 observations
df = pd.DataFrame(data)

# Task 2: Rename the dataframe column names
df.columns = ['Random value 1', 'Random value 2', 'Random value 3', 'Random value 4']

# Task 3: Find the descriptive statistics
descriptive_stats = df.describe()

# Task 4: Check for null values and data types
null_values = df.isnull().sum()
data_types = df.dtypes

# Task 5: Display columns 'Random value 2' & 'Random value 3' with location and index location method
random_value_2_location = df.loc[:, 'Random value 2']
random_value_3_location = df.loc[:, 'Random value 3']

random_value_2_index_location = df.iloc[:, 1]
random_value_3_index_location = df.iloc[:, 2]

print("Task 1: DataFrame with random values:")
print(df)
print("\nTask 2: DataFrame columns renamed:")
print(df)
print("\nTask 3: Descriptive statistics:")
print(descriptive_stats)
print("\nTask 4: Null values and data types:")
print("Null values:")
print(null_values)
print("\nData types:")
print(data_types)
print("\nTask 5: Display 'Random value 2' & 'Random value 3' columns:")
print("Using location method:")
print("Random value 2:")
print(random_value_2_location)
print("\nRandom value 3:")
print(random_value_3_location)
print("\nUsing index location method:")
print("Random value 2:")
print(random_value_2_index_location)
print("\nRandom value 3:")
print(random_value_3_index_location)
