import matplotlib.pyplot as plt
import seaborn as sns

def setup_plot_style():
    """Set up global plot style."""
    plt.style.use('seaborn-darkgrid')

def save_figure(fig, file_name):
    """Save figure to file."""
    fig.savefig(file_name)

def plot_histogram(data, bins=10):
    """Plot histogram."""
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins)
    plt.title('Histogram of Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()
