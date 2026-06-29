# Zbiory danych - Szkolenie Python Wizualizacja Danych

Ten katalog zawiera trzy przykładowe zbiory danych do ćwiczeń podczas szkolenia.

## 1. sprzedaz.csv - Dane sprzedażowe

**Opis:** Dane o sprzedaży produktów elektronicznych w latach 2023-2024.

**Kolumny:**
- `data` - Data transakcji (format: YYYY-MM-DD)
- `produkt` - Nazwa produktu (Laptop, Monitor, Klawiatura, Mysz, Słuchawki, Tablet, Mikrofon, Drukarka)
- `kategoria` - Kategoria produktu (Komputery, Peryferia, Audio)
- `kwota` - Cena jednostkowa produktu w PLN
- `ilosc` - Liczba sprzedanych sztuk

**Liczba rekordów:** 127

**Zastosowanie:**
- Wykresy liniowe (trendy sprzedaży w czasie)
- Wykresy słupkowe (porównanie sprzedaży produktów/kategorii)
- Wykresy kołowe (udział kategorii w całkowitej sprzedaży)
- Analiza sezonowości

## 2. pogoda.csv - Dane pogodowe

**Opis:** Dane pogodowe z wybranych dni w latach 2023-2024 (dla Polski).

**Kolumny:**
- `data` - Data pomiaru (format: YYYY-MM-DD)
- `temperatura` - Temperatura powietrza w stopniach Celsjusza
- `opady` - Suma opadów w mm
- `wilgotnosc` - Wilgotność względna powietrza w %

**Liczba rekordów:** 170

**Zastosowanie:**
- Wykresy liniowe (zmiany temperatury w czasie)
- Wykresy punktowe (scatter plots - korelacje między zmiennymi)
- Histogramy (rozkłady wartości)
- Analiza sezonowości pogody

## 3. pracownicy.csv - Dane pracowników

**Opis:** Dane fikcyjnej firmy o jej pracownikach.

**Kolumny:**
- `id` - Unikalny identyfikator pracownika (1-50)
- `imie` - Imię pracownika
- `wiek` - Wiek w latach (25-60)
- `pensja` - Miesięczne wynagrodzenie brutto w PLN
- `dzial` - Dział firmy (IT, Marketing, Sprzedaż, HR, Finanse)
- `staz` - Staż pracy w latach

**Liczba rekordów:** 50

**Zastosowanie:**
- Wykresy słupkowe (liczba pracowników w działach)
- Wykresy punktowe (wiek vs pensja, staż vs pensja)
- Histogramy (rozkład pensji, wieku)
- Boxploty (porównanie pensji między działami)
- Violinploty (rozkłady w grupach)
- Heatmapy (korelacje między zmiennymi liczbowymi)

## Uwagi

Wszystkie dane są fikcyjne i stworzone wyłącznie na potrzeby szkoleniowe. Wartości zostały wygenerowane tak, aby były realistyczne i pozwalały na ciekawe analizy wizualne.