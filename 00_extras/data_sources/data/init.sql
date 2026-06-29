-- Create table for products
CREATE TABLE IF NOT EXISTS produkty (
    id SERIAL PRIMARY KEY,
    nazwa VARCHAR(100) NOT NULL,
    kategoria VARCHAR(50) NOT NULL,
    cena DECIMAL(10, 2) NOT NULL,
    ilosc INTEGER NOT NULL
);

-- Insert data
INSERT INTO produkty (nazwa, kategoria, cena, ilosc) VALUES
('Laptop Dell XPS', 'Elektronika', 4500.00, 12),
('Mysz Logitech', 'Elektronika', 89.99, 45),
('Klawiatura mechaniczna', 'Elektronika', 350.00, 23),
('Biurko Ikea Bekant', 'Meble', 890.00, 8),
('Krzesło ergonomiczne', 'Meble', 1200.00, 15),
('Lampa biurkowa LED', 'Oświetlenie', 179.99, 34),
('Monitor 27 cali', 'Elektronika', 1299.00, 18),
('Stojak na laptop', 'Akcesoria', 125.50, 28),
('Podkładka pod mysz', 'Akcesoria', 45.00, 67),
('Słuchawki bezprzewodowe', 'Elektronika', 599.00, 22),
('Regał Billy', 'Meble', 349.00, 11),
('Lampka nocna', 'Oświetlenie', 89.00, 42),
('Kabel HDMI 2m', 'Akcesoria', 35.00, 89),
('Powerbank 20000mAh', 'Elektronika', 149.00, 31),
('Mata pod krzesło', 'Akcesoria', 99.00, 19);