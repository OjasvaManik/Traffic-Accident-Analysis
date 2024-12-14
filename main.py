import pandas as pd
from src.data_processing import merge_data
from src.analysis import analyze_accidents_by_cause, analyze_transport_mode, analyze_time_trends
from src.visualization import plot_accidents_by_cause, plot_transport_fatalities, plot_time_trends

# File paths
state_file = "data/raw/StateUTCityAndPlace2018.csv"
cause_file = "data/raw/Cause-wise-2018.csv"
mode_file = "data/raw/Mode-2018.csv"
time_file = "data/raw/TimeOfOccurrence-3Years.csv"
processed_file = "data/processed/merged_data.csv"

def main():
    # Merge datasets
    merged_data = merge_data(state_file, cause_file, mode_file, time_file)
    merged_data.to_csv(processed_file, index=False)
    print("Merged data saved to:", processed_file)

    # Load processed data
    data = pd.read_csv(processed_file)

    # Analysis
    cause_analysis = analyze_accidents_by_cause(data)
    mode_analysis = analyze_transport_mode(data)
    time_analysis = analyze_time_trends(data)

    # Visualizations
    plot_accidents_by_cause(cause_analysis)
    plot_transport_fatalities(mode_analysis)
    plot_time_trends(time_analysis)

if __name__ == "__main__":
    main()
