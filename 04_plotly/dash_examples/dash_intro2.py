from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go



app = Dash()

#Layout
app.layout = html.Div([
    # Tytuł
    html.H1(
        'Dashboard z wieloma kontrolkami',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    # Pierwszy dropdown - typ wykresu
    html.Div([
        html.Label('Typ wykresu:'),
        dcc.Dropdown(
            id='chart-type',
            options=[
                {'label': 'Słupkowy', 'value': 'bar'},
                {'label': 'Liniowy', 'value': 'line'},
                {'label': 'Punktowy', 'value': 'scatter'}
            ],
            value='bar'
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    # Drugi dropdown - kolor
    html.Div([
        html.Label('Kolor:'),
        dcc.Dropdown(
            id='color-choice',
            options=[
                {'label': 'Niebieski', 'value': 'blue'},
                {'label': 'Czerwony', 'value': 'red'},
                {'label': 'Zielony', 'value': 'green'},
                {'label': 'Pomarańczowy', 'value': 'orange'}
            ],
            value='blue'
        )
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),

    html.Br(),
    html.Br(),

    # Wykres
    dcc.Graph(id='dynamic-graph'),

    # Tekst pokazujący wybór
    html.Div(id='selection-info', style={'textAlign': 'center', 'color': '#7f8c8d'})
])

# Callback
# CALLBACK z wieloma Input i Output
@app.callback(
    [Output('dynamic-graph', 'figure'),      # Output 1
     Output('selection-info', 'children')],   # Output 2
    [Input('chart-type', 'value'),            # Input 1
     Input('color-choice', 'value')]          # Input 2
)
def update_graph(chart_type, color):
    """Reaguje na zmiany w OBU dropdown"""

    # Dane
    x_data = ['A', 'B', 'C', 'D']
    y_data = [4, 7, 2 ,5]

    # Wybierz typ wykresu
    if chart_type == 'bar':
        trace = go.Bar(x=x_data, y=y_data, marker={'color': color})
    elif chart_type == 'line':
        trace = go.Scatter(x=x_data, y=y_data, mode='lines+markers', line={'color': color, 'width': 3})
    else:
        trace = go.Scatter(x=x_data, y=y_data, mode='markers', marker={'size': 15, 'color': color})

    # Wykres
    figure = {
        'data': [trace],
        'layout': go.Layout(
            title=f'Wykres {chart_type} w kolorze {color}',
            xaxis={'title': 'Kategoria'},
            yaxis={'title': 'Wartość'}
        )
    }

    # Tekst informacyjny
    info_text = f"Wybrałeś: {chart_type} + {color}"

    # Zwróć OBA wyniki (w kolejności Output)
    return figure, info_text


if __name__ == "__main__":
    app.run(debug=True)
