import numpy as np
import pandas as pd
from scipy.stats import pearsonr

def calculate_statistics(df):
    """Calculate basic statistics."""
    stats = {
        'Mean Price': np.mean(df['Price']),
        'Standard Deviation': np.std(df['Price']),
        'Max Price': np.max(df['Price']),
        'Min Price': np.min(df['Price'])
    }
    return stats

def calculate_correlation(df, columns=['Price', 'Volume']):
    """Calculate correlation matrix."""
    correlation_matrix = df[columns].corr()
    return correlation_matrix

def feature_engineering(df):
    """Perform feature engineering."""
    # Example: Creating lag features
    df['Price Lag 1'] = df['Price'].shift(1)
    df['Price Lag 5'] = df['Price'].shift(5)
    
    return df
