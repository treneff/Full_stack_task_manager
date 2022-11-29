from db.run_sql import run_sql

from models.task import Task
import repositories.user_repository as user_repository
import repositories.project_repository as project_repository


#ADD A TASK TO THE DATABASE
def save(task):
    sql = "INSERT INTO tasks ( title, description, user_id, project_id, completed) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [task.title, task.description, task.user.id, task.project.id, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id

#SELECT A TASK
def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        project = project_repository.select(result['project_id'])
        task = Task(result['title'], result['description'], user, project, result['completed'], result['id'] )
    return task

#SELECT ALL THE TASKS CURRENTLY IN THE DATABASE   
def select_all():
    tasks = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        project = project_repository.select(row['project_id'])
        task = Task(row['title'], row['description'], user, project, row['completed'], row['id'] )
        tasks.append(task)
    return tasks
#Select projects tasks
def select_project_tasks(id):
    tasks_to_display = []
    sql = "SELECT * FROM tasks WHERE project_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for row in results:
            user = user_repository.select(row['user_id'])
            project = project_repository.select(id)
            task = Task(row['title'], row['description'], user, project, row['completed'], row['id'] )
            tasks_to_display.append(task)        
    return tasks_to_display

# SELECT TASKS TO DISPLAY IN PROJECT
def select_project_tasks(id):
    tasks_to_display = []
    sql = "SELECT * FROM tasks WHERE project_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for row in results:
            user = user_repository.select(row['user_id'])
            project = project_repository.select(id)
            task = Task(row['title'], row['description'], user, project, row['completed'], row['id'] )
            tasks_to_display.append(task)        
    return tasks_to_display

# SELECT TASKS TO DISPLAY IN PROJECT
def select_project_tasks(id):
    tasks_to_display = []
    sql = "SELECT * FROM tasks WHERE project_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for row in results:
            user = user_repository.select(row['user_id'])
            project = project_repository.select(id)
            task = Task(row['title'], row['description'], user, project, row['completed'], row['id'] )
            tasks_to_display.append(task)        
    return tasks_to_display

#DELETE A TASK
def delete(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#DELETE ALL TASKS
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)

#UPDATE A TASK
def update(tasks):
    sql = "UPDATE tasks SET (title, description, user_id, project_id, completed) = (%s, %s,%s, %s, %s) WHERE id = %s"
    values = [tasks.title, tasks.description, tasks.user.id, tasks.project.id, tasks.completed, tasks.id]
    run_sql(sql, values)
    
    
    

    

