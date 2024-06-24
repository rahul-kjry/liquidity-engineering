from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model

def fit_arima_model(train_data, order=(1, 0, 0)):
    """Fit ARIMA model."""
    model = ARIMA(train_data, order=order)
    fitted_model = model.fit()
    return fitted_model

def fit_garch_model(train_data):
    """Fit GARCH model."""
    model = arch_model(train_data, vol='Garch', p=1, q=1)
    fitted_model = model.fit()
    return fitted_model
