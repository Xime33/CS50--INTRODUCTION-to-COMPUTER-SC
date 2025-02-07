CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    symbol TEXT,
    shares INTEGER,
    price REAL,
    date TIMESTAMP
);
