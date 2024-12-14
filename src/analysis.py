def analyze_accidents_by_cause(df):
    """Analyze accidents by cause."""
    return df.groupby('Cause')['No. of Cases'].sum()

def analyze_transport_mode(df):
    """Analyze fatalities by mode of transport."""
    return df.groupby('Mode of Transport')['Total Persons Died'].sum()

def analyze_time_trends(df):
    """Analyze accident trends by time of occurrence."""
    return df.groupby('Time Of Occurance')['Accident Count'].sum()
