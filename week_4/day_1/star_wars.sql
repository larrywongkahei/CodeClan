DROP TABLE characters;
DROP TABLE lightsabers;

CREATE TABLE characters(
    id SERIAL,
    name VARCHAR(255),
    darkside BOOLEAN, 
    age INT
);

CREATE TABLE lightsabers(
    id SERIAL, 
    colour VARCHAR(255),
    hilt_metal VARCHAR(255)
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

INSERT INTO lightsabers(colour, hilt_metal) VALUES ('green', 'palladium');
INSERT INTO lightsabers(colour, hilt_metal) VALUES ('red', 'gold');




SELECT * FROM lightsabers;
SELECT * FROM characters;

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