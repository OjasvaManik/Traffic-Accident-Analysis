import pandas as pd

def load_data(file_path):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def preprocess_state_data(file_path):
    """Preprocess the State/UT/City data for analysis."""
    df = load_data(file_path)
    # Example: Summarize Rural and Urban Accident Totals
    df['Rural Total'] = df[['Rural Area (Sub Total) - Total']].sum(axis=1)
    df['Urban Total'] = df[['Urban Area (Sub Total) - Total']].sum(axis=1)
    return df[['State/UT/City', 'Rural Total', 'Urban Total']]

def preprocess_cause_data(file_path):
    """Preprocess the Cause-wise data."""
    df = load_data(file_path)
    df['Total Injuries'] = df[['Persons Injured - Male', 'Persons Injured - Female', 'Persons Injured - Transgender']].sum(axis=1)
    df['Total Deaths'] = df[['Persons Died - Male', 'Persons Died - Female', 'Persons Died - Transgender']].sum(axis=1)
    return df[['Cause', 'No. of Cases', 'Total Injuries', 'Total Deaths']]

def preprocess_mode_data(file_path):
    """Preprocess the Mode of Transport data."""
    df = load_data(file_path)
    return df[['Mode of Transport', 'Total Persons Died', 'Year']]

def preprocess_time_data(file_path):
    """Preprocess the Time of Occurrence data."""
    df = load_data(file_path)
    return df[['Time Of Occurance', 'Accident Count', 'Year']]

def merge_data(state_file, cause_file, mode_file, time_file):
    """Merge preprocessed datasets into a single DataFrame."""
    state_data = preprocess_state_data(state_file)
    cause_data = preprocess_cause_data(cause_file)
    mode_data = preprocess_mode_data(mode_file)
    time_data = preprocess_time_data(time_file)

    # Example of combining relevant datasets (details depend on keys and relationships)
    merged = pd.concat([state_data, cause_data, mode_data, time_data], axis=1)
    return merged

if __name__ == "__main__":
    # File paths
    state_file = "data/raw/StateUTCityAndPlace2018.csv"
    cause_file = "data/raw/Cause-wise-2018.csv"
    mode_file = "data/raw/Mode-2018.csv"
    time_file = "data/raw/TimeOfOccurrence-3Years.csv"
    output_file = "data/processed/merged_data.csv"

    # Merge datasets and save the processed file
    merged_data = merge_data(state_file, cause_file, mode_file, time_file)
    merged_data.to_csv(output_file, index=False)
    print("Data processing complete. Saved merged data to:", output_file)
