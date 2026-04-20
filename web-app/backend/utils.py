import pandas as pd
import numpy as np

def preprocess_data(df):
    """
    Preprocess insurance data
    
    Args:
        df: pandas DataFrame with raw data
    
    Returns:
        Preprocessed DataFrame
    """
    df_processed = df.copy()
    
    # Handle missing values
    df_processed = df_processed.fillna(df_processed.mean(numeric_only=True))
    
    # Remove duplicates
    df_processed = df_processed.drop_duplicates()
    
    # Convert categorical variables to numeric if needed
    for col in df_processed.columns:
        if df_processed[col].dtype == 'object':
            df_processed[col] = pd.factorize(df_processed[col])[0]
    
    return df_processed

def make_prediction(model, data):
    """
    Make predictions using the loaded model
    
    Args:
        model: Loaded ML model
        data: Preprocessed data
    
    Returns:
        Predictions
    """
    try:
        predictions = model.predict(data)
        return predictions.tolist()
    except Exception as e:
        return f"Prediction error: {str(e)}"

def validate_csv(df):
    """
    Validate CSV structure
    
    Args:
        df: pandas DataFrame
    
    Returns:
        Tuple (is_valid, error_message)
    """
    if df.empty:
        return False, "CSV file is empty"
    
    if len(df.columns) == 0:
        return False, "CSV has no columns"
    
    return True, None
