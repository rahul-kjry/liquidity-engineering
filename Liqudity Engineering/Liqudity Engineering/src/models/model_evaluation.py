from sklearn.metrics import accuracy_score, confusion_matrix

def calculate_accuracy(y_true, y_pred):
    """Calculate accuracy score."""
    accuracy = accuracy_score(y_true, y_pred)
    return accuracy

def compute_confusion_matrix(y_true, y_pred):
    """Compute confusion matrix."""
    cm = confusion_matrix(y_true, y_pred)
    return cm
