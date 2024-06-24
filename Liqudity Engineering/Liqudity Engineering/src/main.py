from src.data.data_loader import load_data
from src.data.data_cleaning import clean_data
from src.data.data_analysis import calculate_statistics, calculate_correlation
from src.models.statistical_models import fit_arima_model, fit_garch_model
from src.models.machine_learning_models import train_linear_regression, apply_kmeans_clustering
from src.models.model_evaluation import calculate_accuracy, compute_confusion_matrix
from src.visualization.time_series_plots import plot_time_series
from src.visualization.interactive_plots import plot_interactive_candlestick
from src.utils.logging_utils import setup_logging, log_info, log_error
from src.utils.config import Config

def main():
    # Load and clean data
    df = load_data(Config.DATA_PATH)
    df_cleaned = clean_data(df)
    
    # Data analysis
    stats = calculate_statistics(df_cleaned)
    correlation_matrix = calculate_correlation(df_cleaned)
    
    # Model fitting and evaluation
    arima_model = fit_arima_model(df_cleaned['Price'])
    garch_model = fit_garch_model(df_cleaned['Price'])
    
    # Machine learning models
    X = df_cleaned[['Feature1', 'Feature2']]
    y = df_cleaned['Target']
    regression_model = train_linear_regression(X, y)
    clustering_labels = apply_kmeans_clustering(X)
    
    # Model evaluation
    accuracy = calculate_accuracy(df_cleaned['Actual'], df_cleaned['Predicted'])
    confusion_matrix = compute_confusion_matrix(df_cleaned['Actual'], df_cleaned['Predicted'])
    
    # Visualization
    plot_time_series(df_cleaned)
    plot_interactive_candlestick(df_cleaned)
    
    # Logging
    setup_logging(Config.LOG_FILE)
    log_info("Analysis and visualization completed successfully.")
    
if __name__ == "__main__":
    main()
