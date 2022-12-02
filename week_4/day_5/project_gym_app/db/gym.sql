DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS class_attend;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    membership_level VARCHAR(255),
    gender VARCHAR(255),
    availability VARCHAR(255),
    salary INT,
    status VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    fee INT,
    availability VARCHAR(255),
    duration VARCHAR(255),
    max_capacity INT,
);

CREATE TABLE class_attend (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    classes_id INT REFERENCES classes(id) ON DELETE CASCADE
);
