from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go
from datetime import datetime
import random
from collections import deque  # double-ended queue

app = Dash(__name__)

# Bufor danych - pamiętamy ostatnie 50 punktów
MAX_POINTS = 50
time_data = deque(maxlen=MAX_POINTS)
value_data = deque(maxlen=MAX_POINTS)

app.layout = html.Div([
    html.H1('Live Dashboard - Auto-Refresh',
            style={'textAlign': 'center', 'color': '#2c3e50'}),

    # Aktualna wartość - duża
    html.Div([
        html.H2(id='current-value', style={'color': '#e74c3c'}),
        html.P('Aktualna wartość')
    ], style={'textAlign': 'center'}),

    # Wykres
    dcc.Graph(id='live-update-graph'),

    # Licznik odświeżeń
    html.Div(id='update-count', style={'textAlign': 'center', 'color': '#7f8c8d'}),

    # INTERVAL - automatyczne odświeżanie!
    dcc.Interval(
        id='interval-component',
        interval=1000,  # 1000ms = 1 sekunda
        n_intervals=0   # licznik ticków (automatyczny), rośnie o 1 po każdej sekundzie,
                        # przy callbacku używamy tego jako triggera
    )
])


@app.callback(
    [Output('live-update-graph', 'figure'),
     Output('current-value', 'children'),
     Output('update-count', 'children')],
    Input('interval-component', 'n_intervals')
)
def update_live(n):
    """Wywoływane automatycznie co 1 sekundę!"""

    # Symuluj nowe dane (np. z sensora)
    current_time = datetime.now().strftime('%H:%M:%S')
    new_value = 20 + random.uniform(-5, 5)  # Temperatura 15-25°C

    # Dodaj do bufora
    time_data.append(current_time)
    value_data.append(new_value)

    # Wykres
    figure = {
        'data': [
            go.Scatter(
                x=list(time_data),
                y=list(value_data),
                mode='lines+markers',
                line={'color': '#e74c3c', 'width': 2},
                marker={'size': 6}
            )
        ],
        'layout': go.Layout(
            title='Monitoring w czasie rzeczywistym',
            xaxis={'title': 'Czas'},
            yaxis={'title': 'Temperatura (°C)'},
            hovermode='closest'
        )
    }

    current_display = f"{new_value:.1f} °C"
    count_display = f"Odświeżeń: {n} | Ostatnia aktualizacja: {current_time}"

    return figure, current_display, count_display


if __name__ == '__main__':
    app.run(debug=True)