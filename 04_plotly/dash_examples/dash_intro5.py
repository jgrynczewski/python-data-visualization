from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

# Style wspólne
HEADER_STYLE = {
    'backgroundColor': '#2c3e50',
    'padding': '20px',
    'color': 'white',
    'textAlign': 'center'
}

SECTION_STYLE = {
    'backgroundColor': '#ecf0f1',
    'padding': '20px',
    'margin': '10px',
    'borderRadius': '5px'
}

app.layout = html.Div([
    # HEADER
    html.Div([
        html.H1('📊 Elegancki Dashboard'),
        html.P('Kompletny przykład aplikacji Dash')
    ], style=HEADER_STYLE),

    # KONTROLKI
    html.Div([
        html.H3('Ustawienia'),

        html.Div([
            html.Label('Wybierz funkcję:'),
            dcc.Dropdown(
                id='function-type',
                options=[
                    {'label': 'Sinus', 'value': 'sin'},
                    {'label': 'Cosinus', 'value': 'cos'},
                    {'label': 'Tangens', 'value': 'tan'}
                ],
                value='sin'
            )
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label('Częstotliwość:'),
            dcc.Slider(
                id='frequency',
                min=1,
                max=5,
                step=1,
                value=1,
                marks={i: f'{i}x' for i in range(1, 6)}
            )
        ], style={'width': '60%', 'display': 'inline-block', 'padding': '10px'})
    ], style=SECTION_STYLE),

    # WYKRESY - dwie kolumny
    html.Div([
        html.Div([
            dcc.Graph(id='main-graph')
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(id='secondary-graph')
        ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ]),

    # FOOTER
    html.Div([
        html.P('Dashboard stworzony w Dash | Python + Plotly',
               style={'textAlign': 'center', 'color': '#7f8c8d', 'padding': '20px'})
    ])
])


@app.callback(
    [Output('main-graph', 'figure'),
     Output('secondary-graph', 'figure')],
    [Input('function-type', 'value'),
     Input('frequency', 'value')]
)
def update_graphs(func_type, freq):
    """Aktualizuj oba wykresy"""

    x = np.linspace(0, 4 * np.pi, 200)

    # Wybierz funkcję
    if func_type == 'sin':
        y = np.sin(freq * x)
        title = f'Sinus (f={freq})'
    elif func_type == 'cos':
        y = np.cos(freq * x)
        title = f'Cosinus (f={freq})'
    else:
        y = np.tan(freq * x)
        y = np.clip(y, -10, 10)  # Ograniczamy tangens
        title = f'Tangens (f={freq})'

    # Wykres główny - funkcja
    fig1 = {
        'data': [
            go.Scatter(x=x, y=y, mode='lines',
                       line={'color': '#3498db', 'width': 3})
        ],
        'layout': go.Layout(
            title=title,
            xaxis={'title': 'x'},
            yaxis={'title': 'y'},
            hovermode='closest'
        )
    }

    # Wykres pomocniczy - histogram
    fig2 = {
        'data': [
            go.Histogram(x=y, nbinsx=30,
                         marker={'color': '#e74c3c'})
        ],
        'layout': go.Layout(
            title='Rozkład wartości',
            xaxis={'title': 'Wartość'},
            yaxis={'title': 'Liczba wystąpień'}
        )
    }

    return fig1, fig2


if __name__ == '__main__':
    app.run(debug=True)
