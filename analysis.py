import pandas as pd

# ----------------------------------------------------------------------
# FIX: Manual data cleaning is required because the file is not a standard CSV.
# The code below correctly extracts 'Bloom_Day' from the messy single column.
# ----------------------------------------------------------------------
file_name = r"C:\Users\sumanth\Downloads\plants.csv"
df = pd.read_csv(file_name)

# Get the malformed column name (e.g., 'plants\t Bloom_Days')
malformed_col_name = df.columns[0]

# Split the single malformed column by the comma (',')
df_split = df[malformed_col_name].str.split(',', expand=True)

# Create the final columns
df['Plant_Name'] = df_split[0]

# Clean the 'Bloom_Day' column by removing trailing characters (\t, spaces) and converting to integer
df['Bloom_Day'] = df_split[1].str.replace(r'[\t\s]+', '', regex=True).astype(int)

# Select only the relevant columns for the final DataFrame
df = df[['Plant_Name', 'Bloom_Day']].copy()
# ----------------------------------------------------------------------

print("🌸 Welcome to Bloom Watch 🌸")
print("==============================")

# Step 2: Categorize plants (Your original function, now using the clean 'Bloom_Day' column)
def categorize(day):
    if day < 40:
        return "Early"
    elif day <= 90:
        return "Mid"
    else:
        return "Late"

# This line now works correctly!
df["Category"] = df["Bloom_Day"].apply(categorize)

# Display the final categorized data
print("\nFinal Categorized Data (First 5 Rows):")
print(df.to_string())
