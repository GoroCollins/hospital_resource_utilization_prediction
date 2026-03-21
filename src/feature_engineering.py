import pandas as pd

def create_features(df):
    df = df.copy()
    
    df["target"] = df["patient_count"].shift(-1)
    
    df["lag_1"] = df["patient_count"].shift(1)
    df["lag_3"] = df["patient_count"].shift(3)
    df["lag_7"] = df["patient_count"].shift(7)
    
    df["rolling_mean_3"] = df["patient_count"].rolling(3).mean()
    df["rolling_std_3"] = df["patient_count"].rolling(3).std()
    
    df["day_of_week"] = df.index.dayofweek
    df["is_weekend"] = df["day_of_week"].isin([5,6]).astype(int)
    
    df = df.dropna()
    
    return df