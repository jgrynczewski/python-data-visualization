from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard z Sliderem',
            style={'textAlign': 'center', 'color': '#2c3e50'}),

    # Slider - suwak
    html.Div([
        html.Label('Liczba punktów danych:', style={'fontWeight': 'bold'}),
        dcc.Slider(
            id='num-points',
            min=10,
            max=100,
            step=10,
            value=50,
            marks={i: str(i) for i in range(10, 101, 10)}
        )
    ], style={'padding': '20px'}),

    # Karty ze statystykami
    html.Div([
        html.Div([
            html.H3(id='stat-min', style={'color': '#3498db'}),
            html.P('Minimum')
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center'}),

        html.Div([
            html.H3(id='stat-mean', style={'color': '#2ecc71'}),
            html.P('Średnia')
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center'}),

        html.Div([
            html.H3(id='stat-max', style={'color': '#e74c3c'}),
            html.P('Maximum')
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center'})
    ]),

    # Wykres
    dcc.Graph(id='live-graph')
])


# CALLBACK z 4 Output!
@app.callback(
    [Output('live-graph', 'figure'),
     Output('stat-min', 'children'),
     Output('stat-mean', 'children'),
     Output('stat-max', 'childr en')],
    Input('num-points', 'value')
)
def update_dashboard(n_points):
    """Generuj dane dynamicznie na podstawie slidera"""

    # Generuj losowe dane
    x = np.arange(n_points)
    y = np.random.randn(n_points).cumsum()  # Random walk

    # Wykres
    figure = {
        'data': [
            go.Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                line={'color': '#3498db', 'width': 2},
                marker={'size': 6}
            )
        ],
        'layout': go.Layout(
            title=f'Random Walk - {n_points} punktów',
            xaxis={'title': 'Indeks'},
            yaxis={'title': 'Wartość'},
            hovermode='closest'
        )
    }

    # Statystyki
    min_val = f"{y.min():.2f}"
    mean_val = f"{y.mean():.2f}"
    max_val = f"{y.max():.2f}"

    return figure, min_val, mean_val, max_val


if __name__ == '__main__':
    app.run(debug=True)