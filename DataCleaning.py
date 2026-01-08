import pandas as pd
import numpy as np

# Load your dataset (e.g., from a CSV file)
df = pd.read_csv('your_dataset.csv')
print("Original data shape:", df.shape)
print("Missing values before cleaning:\n", df.isnull().sum())

# --- 1. Handle Missing Values ---
# Option A: Remove rows with any missing values
# Use with caution to avoid losing valuable information
# df = df.dropna()

# Option B: Fill missing values
# For numerical columns, fill with mean or median
df['numeric_col'] = df['numeric_col'].fillna(df['numeric_col'].mean())

# For categorical/text columns, fill with a specific value like 'Unknown' or the mode
df['category_col'] = df['category_col'].fillna('Unknown')

# --- 2. Remove Duplicates ---
# Count and remove duplicate rows
duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows found: {duplicate_count}")
df = df.drop_duplicates()

# --- 3. Correct Data Types ---
# Convert columns to the correct data type (e.g., string to datetime, object to float)
df['date_col'] = pd.to_datetime(df['date_col'])
# df['amount_col'] = df['amount_col'].astype(float)

# --- 4. Clean Text Data ---
# Standardize text by removing whitespace and converting case
df['text_col'] = df['text_col'].str.strip().str.lower()

# Remove unwanted characters using regular expressions
# Example: Keep only letters and spaces
# df['text_col'] = df['text_col'].str.replace(r'[^a-zA-Z\s]', '', regex=True)

# --- 5. Deal with Outliers ---
# Option: Cap values at a certain quantile (e.g., 1st and 99th percentile)
# low, high = df['outlier_col'].quantile([0.01, 0.99])
# df['outlier_col'] = df['outlier_col'].clip(low, high)

# --- 6. Final Check and Export ---
print("\nCleaned data shape:", df.shape)
print("Missing values after cleaning:\n", df.isnull().sum())

# Save the cleaned data to a new CSV file
# df.to_csv('cleaned_dataset.csv', index=False)
