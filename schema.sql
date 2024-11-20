CREATE TABLE refs (
    id SERIAL PRIMARY KEY,
    type TEXT NOT NULL, -- article, book etc.
    ref_name TEXT NOT NULL, -- name for ref in bibtext
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    publisher TEXT
);