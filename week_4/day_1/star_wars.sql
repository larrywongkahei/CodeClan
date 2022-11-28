DROP TABLE lightsabers;

DROP TABLE characters;

CREATE TABLE characters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    darkside BOOLEAN, 
    age INT
);

CREATE TABLE lightsabers(
    id SERIAL PRIMARY KEY, 
    colour VARCHAR(255) NOT NULL,
    hilt_metal VARCHAR(255) NOT NULL,
    characters_id INT REFERENCES characters(id)
);

INSERT INTO characters (name, darkside, age) VALUES ('Obi-Wan Kenobi', true, 27);
INSERT INTO characters (name, darkside, age) VALUES ('Anakin Skywalker', true, 19);
INSERT INTO characters (name, darkside) VALUES ('Darth Maul', true);
INSERT INTO characters (name, darkside, age) VALUES ('Luke Skywalker', false, 17);
INSERT INTO characters (name, darkside , age) VALUES ('Stormroope', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormroope', false, 20);
INSERT INTO characters (name, darkside, age) VALUES ('Stormroope', false, 20);
INSERT INTO characters (name, darkside, age) VALUES ('Stormroope', false, 20);
INSERT INTO characters (name, darkside, age) VALUES ('Stormroope', false, 20);

INSERT INTO lightsabers(colour, hilt_metal, characters_id) VALUES ('green', 'palladium', 2);
INSERT INTO lightsabers(colour, hilt_metal, characters_id) VALUES ('red', 'gold', 2);
INSERT INTO lightsabers(colour, hilt_metal, characters_id) VALUES ('RED', 'COPPER', 3);




SELECT * FROM lightsabers;
SELECT * FROM characters;
SELECT * FROM lightsabers WHERE characters_id = 3

/* 
To create table:
CREATE TABLE  (table name)( column items with the type)

To add itmes into table:
INSERT INTO (column items) VALUES (properties)

To update something:
UPDATE (table) SET (something u want to change)(could add WHERE to update a particular property)

To delete something:
DELETE FROM (table) WHERE something

To run the sql:
SELECT something FROM table
*/