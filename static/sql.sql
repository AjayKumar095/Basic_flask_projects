-- Create the 'books' table
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    units INTEGER
);

-- Insert data into the 'books' table
INSERT INTO books (title, author, units) VALUES
    ('Python Programming', 'Guido van Rossum', 100),
    ('JavaScript Programming', 'Brendan Eich', 120),
    ('Java Programming', 'James Gosling', 90),
    ('C++ Programming', 'Bjarne Stroustrup', 80),
    ('Ruby Programming', 'Yukihiro Matsumoto', 110);
