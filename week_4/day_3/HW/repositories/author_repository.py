from models.author import Author
from db.run_sql import run_sql

def save(author):
    sql = "INSERT INTO authors (name, age, gender) VALUES (%s, %s, %s) RETURNING *"
    VALUES = [author.name, author.age, author.gender]
    result = run_sql(sql, VALUES)
    if result:
        author.id = result[0]['id']

def select_by_id(id):
    sql = "SELECT * FROM authors WHERE id = %s"
    VALUES = [id]
    result = run_sql(sql,VALUES)
    if result :
        result = result[0]
        author = Author(result['name'], result['age'], result['gender'], result['id'])
        return author

def select_all():
    sql = "SELECT * FROM authors"
    VALUES = []
    result = run_sql(sql, VALUES)
    if result:
        for row in result:
            authors = []
            author = Author(row['name'], row['age'], row['gender'], row['id'])
            authors.append(author)
    return authors

def select_by_name(name):
    sql = "SELECT * FROM authors WHERE name = %s"
    VALUES = [name]
    result = run_sql(sql, VALUES)
    if result:
        result = result[0]
        author = Author(result['name'], result['age'], result['gender'], result['id'])
        return author
    return None