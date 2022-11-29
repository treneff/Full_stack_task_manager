from db.run_sql import run_sql

from models.user import User
import repositories.user_repository as user_repository

#ADD A USER
def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id

#SELECT A USER   
def select(id):
    user = None 
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    user = User(result["name"], result["id"])
    return user

#SELECT ALL USERS    
def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['id'] )
        users.append(user)
    return users  

#DELETE A USER
def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE ALL USERS
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)