from db.run_sql import run_sql

def save(member, classes):
    sql = "INSERT INTO class_attend (member_id, classes_id) VALUES (%s, %s)"
    values = [member.id, classes.id]
    run_sql(sql, values)

        

