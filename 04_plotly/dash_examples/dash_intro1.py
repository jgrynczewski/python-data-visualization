from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go


app = Dash()

app.layout = html.Div([
    # Tytuł
    html.H1(
        "Testowa aplikacja Dash",
        style={'textAlign': 'center', 'color': 'blue'}
    ),
    # Paragraf
    html.P("To jeset dashboard zbudowany w Dash z użyciem Plotly"),

    dcc.Dropdown(
        id='chart-type',
        options=[
            {'label': 'Wykres słupkowy', 'value': 'bar'},
            {'label': 'Wykres liniowy', 'value': 'line'},
            {'label': 'Wykres punktowy', 'value': 'scatter'}
        ],
        value='bar'
    ),

    # Wykres Plotly
    dcc.Graph(
        id='static-graph',
        figure={
            'data': [
                go.Bar(x=['A', 'B', 'C', 'D'], y=[4, 7, 2 , 5])
            ],
            'layout': go.Layout(
                title="Prosty wykres słupkowy",
                xaxis={'title': "Kategoria"},
                yaxis={'title': "Wartość"}
            )
        }
    ),

    dcc.Graph(id='dynamic-graph')
])


@app.callback(
    Output('dynamic-graph', 'figure'),
    Input('chart-type', 'value')
)
def update(chart_type):
    X = ['A', 'B', 'C', 'D']
    Y = [4, 7, 2, 5]

    if chart_type == "bar":
        trace = go.Bar(x=X, y=Y)
    elif chart_type == "line":
        trace = go.Scatter(x=X, y=Y, mode='lines+markers')
    else:
        trace = go.Scatter(x=X, y=Y, mode='markers', marker={'size': 50})

    return {
        "data": [trace],
        'layout': go.Layout(
            title=f"Prosty wykres {chart_type}",
            xaxis={'title': "Kategoria"},
            yaxis={'title': "Wartość"}
        )
    }


if __name__ == "__main__":
    app.run(debug=True)