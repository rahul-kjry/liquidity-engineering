import plotly.express as px

def plot_interactive_candlestick(data, title='Interactive Candlestick Chart'):
    """Plot interactive candlestick chart."""
    fig = px.line(data, x=data.index, y='Price', title=title)
    fig.update_xaxes(title='Date')
    fig.update_yaxes(title='Price')
    fig.show()
