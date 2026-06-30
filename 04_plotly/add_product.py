"""
Skrypt do dodawania produktów do bazy PostgreSQL
(do testowania live dashboard)

Uruchom: python add_product.py
"""

from sqlalchemy import create_engine, text
import random

# Konfiguracja bazy (taka sama jak w dashboard)
db_config = {
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5433',
    'database': 'produkty_db'
}

connection_string = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
engine = create_engine(connection_string)

# Przykładowe dane do losowania
produkty_przykladowe = {
    'Elektronika': [
        ('Laptop Dell', 3500),
        ('iPhone 15', 4500),
        ('Słuchawki Sony', 899),
        ('Tablet Samsung', 1200),
        ('Smartwatch Apple', 1899),
        ('Klawiatura Logitech', 450),
        ('Myszka Razer', 299)
    ],
    'Książki': [
        ('Python dla zaawansowanych', 89),
        ('Django w praktyce', 79),
        ('Machine Learning', 120),
        ('SQL od podstaw', 65),
        ('Clean Code', 99)
    ],
    'Odzież': [
        ('Kurtka zimowa', 450),
        ('Buty sportowe Nike', 399),
        ('Bluza Adidas', 199),
        ('Spodnie jeansowe', 149)
    ],
    'Sport': [
        ('Rower górski', 2500),
        ('Piłka nożna', 89),
        ('Rakieta tenisowa', 450),
        ('Mata do jogi', 79)
    ]
}

def dodaj_losowy_produkt():
    """Dodaje losowy produkt do bazy"""
    # Losuj kategorię
    kategoria = random.choice(list(produkty_przykladowe.keys()))

    # Losuj produkt z tej kategorii
    nazwa, cena = random.choice(produkty_przykladowe[kategoria])

    # Dodaj timestamp do nazwy (żeby był unikalny)
    from datetime import datetime
    timestamp = datetime.now().strftime('%H%M%S')
    nazwa_unikalna = f"{nazwa} #{timestamp}"

    # INSERT do bazy (z ilością - losowa 1-50)
    ilosc = random.randint(1, 50)
    query = f"""
    INSERT INTO produkty (nazwa, cena, kategoria, ilosc)
    VALUES ('{nazwa_unikalna}', {cena}, '{kategoria}', {ilosc})
    """

    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()

    print(f"✅ Dodano: {nazwa_unikalna} ({cena} zł) - {kategoria}")

def menu():
    """Interaktywne menu"""
    print("\n" + "="*50)
    print("DODAWANIE PRODUKTÓW DO BAZY POSTGRESQL")
    print("="*50)
    print("1. Dodaj 1 losowy produkt")
    print("2. Dodaj 5 losowych produktów")
    print("3. Dodaj 10 losowych produktów")
    print("4. Usuń ostatnie 5 produktów")
    print("0. Wyjście")
    print("="*50)

    wybor = input("Wybierz opcję (0-4): ")

    if wybor == '1':
        dodaj_losowy_produkt()
    elif wybor == '2':
        for _ in range(5):
            dodaj_losowy_produkt()
    elif wybor == '3':
        for _ in range(10):
            dodaj_losowy_produkt()
    elif wybor == '4':
        usun_ostatnie(5)
    elif wybor == '0':
        print("👋 Do zobaczenia!")
        return False
    else:
        print("❌ Nieprawidłowy wybór!")

    return True

def usun_ostatnie(ile):
    """Usuwa ostatnie N produktów"""
    query = f"""
    DELETE FROM produkty
    WHERE id IN (
        SELECT id FROM produkty
        ORDER BY id DESC
        LIMIT {ile}
    )
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))
        conn.commit()

    print(f"🗑️  Usunięto ostatnie {ile} produktów")

if __name__ == '__main__':
    print("\n🚀 Dashboard musi być uruchomiony: python postgres_live_dashboard.py")
    print("💡 Ten skrypt dodaje produkty - zobacz jak wykres się zmienia!\n")

    # Pętla menu
    while menu():
        pass