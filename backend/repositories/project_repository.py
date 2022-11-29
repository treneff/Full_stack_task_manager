from db.run_sql import run_sql

from models.project import Project
import repositories.project_repository as project_repository
import repositories.task_repository as task_repository
from models.task import Task

#save a project
def save(project):
    sql = "INSERT INTO projects (name) VALUES (%s) RETURNING id"
    values = [project.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    project.id = id             

#select a project
def select(id):
    project = None 
    sql = "SELECT * FROM projects WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    project = Project(result["name"], result["id"])
    return project

# select all projects
def select_all():
    projects = []
    sql = "SELECT * FROM projects"
    results = run_sql(sql)
    for row in results:
        project = Project(row['name'], row['id'] )
        projects.append(project)
    return projects

#DELETE A PROJECT
def delete(id):
    sql = "DELETE FROM projects WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#DELETE ALL PROJECTS
def delete_all():
    sql = "DELETE FROM projects"
    run_sql(sql)