import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Puhastan andmed.

data = pd.read_csv('Liiklusõnnetused_2011_2021.csv')

# Generating descriptive statistics for numerical columns
numerical_summary = data.describe()

# Checking data types and missing values
data_types_missing = pd.DataFrame({
    'Data Type': data.dtypes,
    'Missing Values': data.isnull().sum(),
    'Percentage Missing': (data.isnull().sum() / len(data)) * 100
})

print(numerical_summary, data_types_missing.head(10))  # Displaying the first 10 columns for data types and missing values info


columns_to_drop = ['Maja nr (PPA)', 'Ristuv tänav (PPA)', 'Asula','Tee tüüp [1]','Tee nr (PPA)','Tee km (PPA)',]
data.drop(columns=columns_to_drop, inplace=True)

data.columns
