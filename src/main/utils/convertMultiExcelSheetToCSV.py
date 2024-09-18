import pandas as pd


def create_csv_from_excel(excel_file):
    # Read all sheets from the Excel file into a dictionary of DataFrames
    all_sheets_dict = pd.read_excel(excel_file, sheet_name=None, engine='openpyxl')

    # Create a Empty dictionary to store the DataFrames
    # This dictionary will store each sheet's DataFrame keyed by sheet name
    dataframes = {}

    # Loop through the dictionary of DataFrames
    for sheet_name, df in all_sheets_dict.items():
        # Define a CSV file name for this sheet
        csv_file = f'../../resources/metabolamics/{sheet_name}.csv'

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)

        # Read the CSV file back into a DataFrame (optional, if you need to work with it immediately)
        dataframes[sheet_name] = pd.read_csv(csv_file)

    return dataframes

def main():
    # Create CSV files from an Excel file
    dataframes = create_csv_from_excel(
        '../../resources/metabolamics/Antino_BT_Lipid_QE_data_grouped_based_on_class_pos.xlsx')
    # Print the first few rows of each DataFrame
    for sheet_name, df in dataframes.items():
        print(f'\n{sheet_name}')
        print(df.head())

if __name__ == '__main__':
    main()