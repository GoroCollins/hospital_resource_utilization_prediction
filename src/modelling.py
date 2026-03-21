import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def train_test_split_time_series(df, target_col="target", test_size=0.2):
    split_index = int(len(df) * (1 - test_size))
    
    train = df.iloc[:split_index]
    test = df.iloc[split_index:]
    
    X_train = train.drop(columns=[target_col])
    y_train = train[target_col]
    
    X_test = test.drop(columns=[target_col])
    y_test = test[target_col]
    
    return X_train, X_test, y_train, y_test


def evaluate(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    
    return {"MAE": mae, "RMSE": rmse}