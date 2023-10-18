import pyarrow.parquet as pq
import os

# Specify the folder containing the Arrow files
folder_path = r"C:\Users\kinla\Documents\All_github_repo\datasets\gutenberg\train"

# List all the Arrow files in the folder
arrow_files = [file for file in os.listdir(folder_path) if file.endswith('.arrow')]

# Load all Arrow files and concatenate them into a single table
tables = [pq.read_table(os.path.join(folder_path, file)) for file in arrow_files]
full_table = pq.concat_tables(tables)

# Convert the Arrow table to a Pandas DataFrame for further analysis
df = full_table.to_pandas()

# Now you can work with the 'df' DataFrame
print(df)
