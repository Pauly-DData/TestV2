#Dit is een test voor git en github
import pandas as pd

def delete_first_five_columns(file_path, output_base_path, version=3):

    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if dataframe has at least 5 columns
    if df.shape[1] < 5:
        raise ValueError("The input CSV file must have at least 5 columns.")
    
    # Delete the first 5 columns
    df = df.iloc[:, 5:]
    
    # Save the modified dataframe to a new CSV file with version number
    output_path = f"{output_base_path}_v{version}.csv"
    df.to_csv(output_path, index=False)
    
    return df

# Usage of the function with your file
input_file_path = 'Stichting Park Medisch Centrum Verbruik Dataset V2.csv'
output_base_path = 'Stichting Park Medisch Centrum Verbruik Dataset'

# Using the function to read, modify, and save the data
try:
    modified_df = delete_first_five_columns(input_file_path, output_base_path, version=3)
    print(f"Modified data saved to {output_base_path}_v3.csv")
except Exception as e:
    print(f"An error occurred: {str(e)}")
