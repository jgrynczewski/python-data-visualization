"""
Dashboard Dash z live odświeżaniem danych z PostgreSQL

Uruchom: python postgres_live_dashboard.py
Otwórz: http://127.0.0.1:8050/

DEMO:
Podczas gdy dashboard działa, dodaj nowy produkt do bazy:
INSERT INTO produkty (nazwa, cena, kategoria) VALUES ('Nowy produkt', 199, 'Elektronika');

Wykres automatycznie się zaktualizuje!
"""

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine

# ========================
# KONFIGURACJA BAZY DANYCH
# ========================

db_config = {
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5433',
    'database': 'produkty_db'
}

# Connection string
connection_string = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

# Utwórz engine (globalny - będzie reużywany)
engine = create_engine(connection_string)

print("✅ Połączono z bazą PostgreSQL")

# ========================
# APLIKACJA DASH
# ========================

app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1('📊 Live Dashboard - PostgreSQL',
            style={'textAlign': 'center', 'color': '#2c3e50'}),

    html.P('Dashboard odświeża się co 1 sekundę. Dodaj produkt do bazy i zobacz zmianę!',
           style={'textAlign': 'center', 'color': '#7f8c8d'}),

    # Statystyka - liczba produktów
    html.Div([
        html.H2(id='total-count', style={'color': '#e74c3c'}),
        html.P('Łączna liczba produktów w bazie')
    ], style={'textAlign': 'center', 'padding': '20px'}),

    # Wykres
    dcc.Graph(id='live-graph'),

    # Info o ostatniej aktualizacji
    html.Div(id='update-info', style={'textAlign': 'center', 'color': '#95a5a6', 'padding': '10px'}),

    # Interval - odświeżanie co 1 sekundę
    dcc.Interval(
        id='interval-component',
        interval=1000,  # 1000ms = 1 sekunda
        n_intervals=0
    )
])

# Callback - aktualizacja wykresu
@app.callback(
    [Output('live-graph', 'figure'),
     Output('total-count', 'children'),
     Output('update-info', 'children')],
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    """
    Ta funkcja jest wywoływana automatycznie co 1 sekundę.
    Pobiera świeże dane z bazy i aktualizuje wykres.
    """

    # Query do bazy - liczba produktów per kategoria
    query = """
    SELECT
        kategoria,
        COUNT(*) as liczba_produktow
    FROM produkty
    GROUP BY kategoria
    ORDER BY liczba_produktow DESC
    """

    # Wczytaj dane z bazy (ŚWIEŻE!)
    df = pd.read_sql_query(query, engine)

    # Wykres słupkowy
    fig = px.bar(
        df,
        x='kategoria',
        y='liczba_produktow',
        title='Liczba produktów według kategorii (LIVE)',
        labels={'kategoria': 'Kategoria', 'liczba_produktow': 'Liczba produktów'},
        color='liczba_produktow',
        color_continuous_scale='Blues',
        text='liczba_produktow'
    )

    # Dostosuj wygląd
    fig.update_traces(
        texttemplate='%{text}',
        textposition='outside'
    )

    fig.update_layout(
        xaxis_tickangle=-45,
        height=500,
        hovermode='x'
    )

    # Łączna liczba produktów
    total = df['liczba_produktow'].sum()
    total_display = f"{total} produktów"

    # Info o aktualizacji
    from datetime import datetime
    update_time = datetime.now().strftime('%H:%M:%S')
    update_info = f"Ostatnia aktualizacja: {update_time} | Odświeżeń: {n}"

    return fig, total_display, update_info

if __name__ == '__main__':
    print("🚀 Uruchamianie dashboardu...")
    print("📊 Otwórz przeglądarkę: http://127.0.0.1:8050/")
    print("⏹️  Zatrzymaj: Ctrl+C")
    print("")
    print("💡 DEMO: Dodaj produkt do bazy podczas gdy dashboard działa:")
    print("   INSERT INTO produkty (nazwa, cena, kategoria) VALUES ('Test', 99, 'Elektronika');")
    print("")
    app.run(debug=True)