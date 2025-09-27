CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

-- Insert sample data
INSERT INTO flights (origin, destination, duration)
VALUES 
('Addis Ababa', 'Nairobi', 120),
('Addis Ababa', 'Dubai', 240),
('Addis Ababa', 'Cairo', 180);