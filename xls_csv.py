import pandas as pd
import os

# Define the folder containing the Excel files
input_folder = '/'
output_folder = '/'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get a list of all Excel files in the input folder
excel_files = [f for f in os.listdir(input_folder) if f.endswith(('.xls', '.xlsx'))]

# Loop through the list and convert each file to CSV
for excel_file in excel_files:
    # Create full file path
    excel_path = os.path.join(input_folder, excel_file)
    # Read the Excel file
    df = pd.read_excel(excel_path)
    # Create the CSV file path
    csv_file = os.path.splitext(excel_file)[0] + '.csv'
    csv_path = os.path.join(output_folder, csv_file)
    # Write DataFrame to CSV
    df.to_csv(csv_path, index=False)

print(f'Converted {len(excel_files)} Excel files to CSV.')
