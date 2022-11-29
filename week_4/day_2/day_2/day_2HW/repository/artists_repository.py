from db.run_sql import run_sql

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    VALUES = [artist.name]
    results = run_sql(sql, VALUES)
    artist.id = results[0]['id']

def delete_all():
    sql = "DELETE FROM artists"
    values = []
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def list_all_album(artist):
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [artist.id]
    run_sql(sql, values)