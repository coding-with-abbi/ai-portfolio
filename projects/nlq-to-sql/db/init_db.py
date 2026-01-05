import duckdb
import os

# Lösche die Datenbank, falls sie beschädigt ist
db_path = "db/analytics.db"
if os.path.exists(db_path):
    try:
        # Versuche die Datenbank zu öffnen, um zu prüfen ob sie gültig ist
        test_con = duckdb.connect(db_path)
        test_con.close()
    except Exception:
        # Wenn Fehler auftritt, lösche die Datei
        os.remove(db_path)
        print("Removed corrupted database file.")

con = duckdb.connect(db_path)

con.execute("""
CREATE TABLE IF NOT EXISTS sales (
    date DATE,
    region TEXT,
    product TEXT,
    revenue FLOAT
)
""")

con.execute("""
INSERT INTO sales VALUES
('2024-01-01', 'EU', 'A', 1200),
('2024-01-02', 'EU', 'B', 800),
('2024-01-01', 'US', 'A', 1500),
('2024-01-03', 'US', 'C', 2000)
""")

con.close()
print("Database initialized.")

