from db.run_sql import run_sql

# To Save a new member to members table
def save(new_member):
    sql = """INSERT INTO members (membership_level, gender, availability, salary, status) 
    VALUES (%s, %s, %s, %s, %s) RETURNING *"""
    values = [new_member.membership_level, new_member.gender, new_member.availability, new_member.salary, new_member.status]
    result = run_sql(sql, values)
    if result:
        new_member.id = result[0]['id']

# To Delete a member from members table
def delete_by_id(member_id):
    sql = "DELETE FROM members WHERE members.id = %s"
    values = [member_id]
    run_sql(sql, values)


