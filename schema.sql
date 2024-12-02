CREATE TABLE refs (
    id SERIAL PRIMARY KEY,
    type TEXT NOT NULL, -- article, book or inproceedings
    ref_name TEXT NOT NULL, -- name for ref in bibtext

    author TEXT,
    title TEXT,
    journal TEXT,
    year INTEGER,
    volume TEXT,
    pages TEXT,
    month TEXT,
    doi TEXT,
    note TEXT,
    key TEXT,

    publisher TEXT,
    series TEXT,
    address TEXT,
    edition TEXT,
    url TEXT,

    booktitle TEXT,
    editor TEXT,
    organization TEXT
);
