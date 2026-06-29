# Wczytywanie danych z zewnętrznych źródeł

Materiały do nauki wczytywania danych z różnych formatów i źródeł.

## Struktura

```
00_extras/data_sources/
├── data/
│   ├── produkty.csv           # Dane w formacie CSV
│   ├── produkty.json          # Dane w formacie JSON
│   ├── produkty.xlsx          # Dane w formacie Excel
│   ├── produkty.db            # Baza danych SQLite
│   └── init.sql               # Skrypt inicjalizacyjny dla PostgreSQL
├── setup/
│   ├── 00_docker_intro.ipynb  # Wprowadzenie do Dockera
│   ├── docker-compose.yml     # Konfiguracja PostgreSQL w Docker
├── 01_csv.ipynb               # Wczytywanie z pliku CSV
├── 02_json.ipynb              # Wczytywanie z pliku JSON
├── 03_excel.ipynb             # Wczytywanie z pliku Excel
├── 04_api.ipynb               # Wczytywanie z API
├── 05_sqlite.ipynb            # Wczytywanie z bazy SQLite
├── 06_postgresql.ipynb        # Wczytywanie z bazy PostgreSQL

```

## Dane

Wszystkie formaty zawierają te same dane - 15 produktów z 4 kategoriami:
- **nazwa** - nazwa produktu
- **kategoria** - kategoria (Elektronika, Meble, Oświetlenie, Akcesoria)
- **cena** - cena w zł
- **ilosc** - ilość na stanie

## Instalacja zależności

```bash
pip install pandas matplotlib openpyxl requests psycopg2-binary sqlalchemy
```

## PostgreSQL - Setup z Docker

**Jeśli nie znasz Dockera:** Zobacz `00_docker_intro.ipynb` - proste wprowadzenie do Dockera i Docker Compose.

1. Uruchom kontener PostgreSQL:
```bash
cd 00_extras/data_sources
docker-compose up -d
```

2. Sprawdź status:
```bash
docker-compose ps
```

3. Baza zostanie automatycznie zainicjalizowana danymi z `data/init.sql`

4. Zatrzymaj kontener:
```bash
docker-compose down
```

5. Usuń dane (jeśli chcesz zacząć od nowa):
```bash
docker-compose down -v
```

## Notatniki

Każdy notatnik zawiera:
1. Wprowadzenie do formatu/źródła
2. Wczytanie danych
3. Podstawową eksplorację
4. Identyczną wizualizację (Top 5 najdroższych produktów)

### Kolejność nauki (rekomendowana):

0. **00_docker_intro.ipynb** - wprowadzenie do Dockera (opcjonalne, ale pomocne przed PostgreSQL)
1. **01_csv.ipynb** - najprostszy format
2. **02_json.ipynb** - format używany w API
3. **03_excel.ipynb** - format biznesowy
4. **05_sqlite.ipynb** - lokalna baza danych
5. **04_api.ipynb** - pobieranie z API
6. **06_postgresql.ipynb** - produkcyjna baza danych (wymaga Dockera)

## Wizualizacja

Wszystkie notatniki kończą się tym samym wykresem słupkowym:
- Tytuł: "Top 5 najdroższych produktów"
- Oś X: Nazwa produktu
- Oś Y: Cena (zł)
- Kolor: steelblue

## Dodatkowe informacje

### CSV
- Separator: przecinek (`,`)
- Kodowanie: UTF-8
- Nagłówek: pierwszy wiersz

### JSON
- Format: tablica obiektów
- Kodowanie: UTF-8

### Excel
- Format: `.xlsx`
- Arkusz: "Produkty"
- Wymaga: `openpyxl`

### SQLite
- Plik: `produkty.db`
- Tabela: `produkty`
- Wbudowana w Python (moduł `sqlite3`)

### PostgreSQL
- Host: localhost
- Port: 5432
- User: postgres
- Password: postgres
- Database: produkty_db
- Tabela: produkty
- Wymaga: `psycopg2-binary`, `sqlalchemy`

### API
- Przykład z publicznym API: JSONPlaceholder
- Symulacja API dla produktów
- Obsługa błędów i timeout
- Wymaga: `requests`