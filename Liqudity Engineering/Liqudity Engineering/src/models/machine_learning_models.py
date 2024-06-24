from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error

def train_linear_regression(X_train, y_train):
    """Train linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def apply_kmeans_clustering(data, num_clusters=3):
    """Apply K-means clustering."""
    kmeans = KMeans(n_clusters=num_clusters)
    labels = kmeans.fit_predict(data)
    return labels

def evaluate_model_performance(model, X_test, y_test):
    """Evaluate model performance."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse
