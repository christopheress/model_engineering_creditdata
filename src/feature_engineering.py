# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import excel data
df_fees = pd.read_excel('/Users/christopheressmann/Documents/GitHub/model_engineering_creditdata/data/raw/PSP_Fees.xlsx')
df_psp = pd.read_excel('/Users/christopheressmann/Documents/GitHub/model_engineering_creditdata/data/raw/PSP_Jan_Feb_2019.xlsx')

# Merge the fees DataFrame with the original dataset based on 'PSP' and 'success'
df_merged = pd.merge(df_psp, df_fees, on=['PSP', 'success'], how='left')

# Show the first few rows of the merged DataFrame to verify
df_merged.head()