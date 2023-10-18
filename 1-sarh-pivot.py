import pandas as pd

# Define the file path and worksheet name
file_path = "/Users/femisokoya/Documents/GitHub/1-sarh/sarh0112.xls"
worksheet_name = "2022_23"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=worksheet_name)

# Define a dictionary to map Base names to ONS codes
base_to_ons = {
    "Stornoway": "S12000033",
    "Humberside": "E06000011",
    "Newquay": "E06000052",
    "Inverness": "S12000027",
    "Lydd": "E04004358",
    "Sumburgh": "S12000017",
    "Lee On Solent": "E04012176",
    "Prestwick": "S12000028",
    "St Athan": "W06000015",
    "Caernarfon": "W06000002",
}

# Insert the "ONS_code" column after the third column
df.insert(3, "ONS_code", df["Base"].map(base_to_ons))

# Define the index columns
index_columns = ['Date', 'Day of week', 'Base', 'ONS_code', 'Type of tasking', 'Tasking location', 'Tasking outcome', 'Region']

# Pivot the DataFrame using the specified index columns
df = df.pivot_table(index=index_columns)

# Reset the index to make the index columns regular columns
df = df.reset_index()

# Save the DataFrame to a CSV file
df.to_csv("result_pivot.csv", index=False)

print("CSV file saved as result_pivot.csv")
