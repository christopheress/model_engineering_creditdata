import streamlit as st
import pandas as pd
from datetime import datetime

# Load the Excel file into a DataFrame
file_path = '../data/raw/PSP_Jan_Feb_2019.xlsx'
df = pd.read_excel(file_path)

# Let's assume a base fee rate of 2% of the transaction amount
base_fee_rate = 0.02

# Define a function to calculate fees and success rate for a given date range
def calculate_metrics(df, start_date, end_date):
    # Filter the DataFrame based on the date range
    df_filtered = df[(df['tmsp'] >= start_date) & (df['tmsp'] <= end_date)]

    # Calculate the total fees
    total_fees = (df_filtered['amount'] * base_fee_rate).sum()

    # Calculate the success rate
    if len(df_filtered) > 0:
        success_rate = df_filtered['success'].mean() * 100  # in percentage
    else:
        success_rate = 0.0  # No transactions in the date range

    return total_fees, success_rate

# Test the function with an example date range
start_date = datetime(2019, 1, 1)
end_date = datetime(2019, 1, 31)
calculate_metrics(df, start_date, end_date)

#%%
# Load the data
def load_data():
    df = pd.read_excel(file_path)
    return df

df = load_data()

# Sidebar: Date range selection
st.sidebar.title("Date Range Selection")
min_date = df['tmsp'].min().date()
max_date = df['tmsp'].max().date()
start_date = st.sidebar.date_input("Start Date", min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input("End Date", min_value=min_date, max_value=max_date, value=max_date)

# Calculate metrics
base_fee_rate = 0.02
df_filtered = df[(df['tmsp'] >= pd.Timestamp(start_date)) & (df['tmsp'] <= pd.Timestamp(end_date))]
total_fees = (df_filtered['amount'] * base_fee_rate).sum()
if len(df_filtered) > 0:
    success_rate = df_filtered['success'].mean() * 100  # in percentage
else:
    success_rate = 0.0

# Sidebar: Fee Factor
st.sidebar.title("Fee Factor")
fee_factor = st.sidebar.slider("Adjust the fee factor", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
adjusted_fees = total_fees * fee_factor

# Display metrics
st.title("Machine Learning Model Dashboard")
st.header("Before / After Comparison")
st.write(f"Total Fees (Before Adjustment): {total_fees}")
st.write(f"Total Fees (After Adjustment): {adjusted_fees}")
st.write(f"Success Rate: {success_rate}%")

# Additional business metrics can be added here, like plotting the transaction volume over time, etc.

#%%
