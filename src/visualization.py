import matplotlib.pyplot as plt
import seaborn as sns

def plot_accidents_by_cause(cause_analysis):
    """Plot accidents by cause."""
    plt.figure(figsize=(12, 6))
    sns.barplot(x=cause_analysis.index, y=cause_analysis.values, palette="muted")
    plt.title("Accidents by Cause", fontsize=16)
    plt.xticks(rotation=45, ha="right")  # Rotate labels and align to the right
    plt.xlabel("Cause", fontsize=12)
    plt.ylabel("Number of Cases", fontsize=12)
    plt.tight_layout()  # Automatically adjust layout to avoid overlapping
    plt.show()


def plot_transport_fatalities(mode_analysis):
    """Plot fatalities by mode of transport."""
    plt.figure(figsize=(10, 5))
    sns.barplot(x=mode_analysis.index, y=mode_analysis.values, palette="coolwarm")
    plt.title("Fatalities by Mode of Transport", fontsize=16)
    plt.xticks(rotation=30, ha="right")  # Slight rotation for readability
    plt.xlabel("Mode of Transport", fontsize=12)
    plt.ylabel("Total Fatalities", fontsize=12)
    plt.tight_layout()  # Adjust layout to fit elements
    plt.show()


def plot_time_trends(time_analysis):
    """Plot accident trends by time of occurrence."""
    plt.figure(figsize=(10, 5))  # Slightly larger for better readability
    sns.lineplot(x=time_analysis.index, y=time_analysis.values, marker='o', linewidth=2, color="b")
    plt.title("Accidents by Time of Occurrence", fontsize=16)
    plt.xlabel("Time of Occurrence", fontsize=12)
    plt.ylabel("Accident Count", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)  # Add light grid for clarity
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels if needed
    plt.tight_layout()
    plt.show()

