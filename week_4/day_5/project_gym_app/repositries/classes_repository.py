from db.run_sql import run_sql

# Save a class into the classes table
def save(new_class):
    sql = """INSERT INTO classes (fee, availability, duration, max_capacity) 
    VALUES (%s, %s, %s, %s) RETURNING *"""
    values = [new_class.fee, new_class.availability, new_class.duration, new_class._capacity]
    result = run_sql(sql, values)
    if result:
        new_class.id = result[0]['id']

# To Delete a class from classes table
def delete_by_id(class_id):
    sql = "DELETE FROM classes WHERE classes.id = %s"
    values = [class_id]
    run_sql(sql, values)

