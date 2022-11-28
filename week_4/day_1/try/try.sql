DROP TABLE hihi;

CREATE TABLE hihi(
    name VARCHAR(30),
    checkout BOOLEAN
);

INSERT INTO hihi (name, checkout) VALUES ('little prince', false);
INSERT INTO hihi (name, checkout) VALUES ('haha', true);

DELETE FROM hihi WHERE name = 'haha';

UPDATE hihi SET name = 'little princess' WHERE name = 'little prince';

SELECT * FROM hihi;