from db.run_sql import run_sql

def save(album):
    sql = "INSERT INTO albums (name, title, genre, artists_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.name, album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    album.id = results[0]['id']

def delete_all():
    sql = "DELETE FROM albums"
    values = []
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)
