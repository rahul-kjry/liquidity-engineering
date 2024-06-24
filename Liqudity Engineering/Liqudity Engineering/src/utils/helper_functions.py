import numpy as np

def calculate_moving_average(data, window_size=30):
    """Calculate moving average."""
    moving_avg = np.convolve(data, np.ones(window_size)/window_size, mode='valid')
    return moving_avg

def normalize_data(data):
    """Normalize data."""
    normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return normalized_data
