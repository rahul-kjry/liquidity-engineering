import matplotlib.pyplot as plt

def plot_time_series(data, column='Price', title='Time Series Plot'):
    """Plot time series."""
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data[column], marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
