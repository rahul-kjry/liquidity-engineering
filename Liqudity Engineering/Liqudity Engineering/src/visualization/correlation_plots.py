import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(data):
    """Plot correlation heatmap."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap')
    plt.show()
