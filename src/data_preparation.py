import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    # Standardize column names
    df.columns = df.columns.str.lower()
    
    df["appointmentday"] = pd.to_datetime(df["appointmentday"]).dt.tz_localize(None)
    df["scheduledday"] = pd.to_datetime(df["scheduledday"]).dt.tz_localize(None)
    # Rename columns
    df.rename(columns={"no-show": "no_show"}, inplace=True)
    
    return df


def filter_attended(df):
    return df[df["no_show"] == "No"].copy()


def create_daily_series(df):
    daily = (
        df.groupby("appointmentday").size().rename("patient_count").reset_index())
    
    daily = daily.sort_values("appointmentday")
    daily.set_index("appointmentday", inplace=True)
    
    daily = daily.asfreq("D")
    daily["patient_count"] = daily["patient_count"].fillna(0)
    
    return daily