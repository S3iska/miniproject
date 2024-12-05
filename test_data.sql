INSERT INTO refs (id, ref_type, ref_name, author, title, year, journal)
VALUES (100, 'article', 'ref1', 'John Doe', 'Dah Wah', 1999, 'ABC'),
(101, 'article', 'reftwo', 'Jack Black', 'Rock Schule', 1980, 'Otava');

INSERT INTO tags (tag_id, tag_name)
VALUES  (100, 'Intel'),
        (101, 'AMD');

INSERT INTO ref_tags (ref_id, tag_id)
VALUES  (100, 100), (100, 101), (101, 101);
