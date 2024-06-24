import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(df):
    """Clean and preprocess data."""
    # Example: Handling missing values
    df.fillna(method='ffill', inplace=True)
    
    # Example: Normalization
    scaler = StandardScaler()
    df['Normalized Price'] = scaler.fit_transform(df[['Price']])
    
    return df

def remove_outliers(df):
    """Remove outliers from data."""
    # Example: Removing outliers using Z-score
    z_scores = np.abs(stats.zscore(df['Price']))
    df_cleaned = df[(z_scores < 3)]
    
    return df_cleaned
