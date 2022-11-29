from flask import Blueprint, Flask, redirect, render_template, request

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository
import repositories.project_repository as project_repository
from models.task import Task
from models.project import Project
from models.task import Task


projects_blueprint = Blueprint("projects", __name__)
#ROUTE ALL TASKS
@projects_blueprint.route("/projects")
def all_projects():
    projects = project_repository.select_all()
    return render_template("projects/index_projects.html", projects = projects)

#ROUTE NEW PROJECT
@projects_blueprint.route("/projects/new")
def new_project():
    projects = project_repository.select_all()
    return render_template("projects/new.html", projects=projects)

#ROUTE CREATE NEW PROJECT
@projects_blueprint.route("/projects", methods=["POST"])
def create_project():
    name = request.form["name"]
    new_project = Project(name)
    project_repository.save(new_project)
    return redirect("/projects")

#ROUTE DELETE A PROJECT
@projects_blueprint.route("/projects/<id>/delete", methods=['POST'])
def delete_project(id):
    project_repository.delete(id)
    return redirect('/projects')

#ROUTE SHOW A TASK IN PROJECT
@projects_blueprint.route("/projects/<project_id>/tasks/<id>", methods=['GET'])
def show_task_in_project(project_id,id):
    task = task_repository.select(id)
    project = project_repository.select(project_id)
    projects = project_repository.select_all()
    return render_template('tasks/show.html', task = task, project = project, projects = projects)

#ROUTE SHOW ALL TASKS 
@projects_blueprint.route("/projects/<id>/tasks")
def projects_tasks(id):
    tasks = task_repository.select_project_tasks(id)
    project = project_repository.select(id)
    return render_template("projects/project_tasks.html",tasks = tasks, project = project)

#ROUTE NEW TASK PAGE
@projects_blueprint.route("/projects/<id>/tasks/new")
def new_project_task(id):
    users = user_repository.select_all()
    project = project_repository.select(id)
    projects = project_repository.select_all()
    return render_template("tasks/new.html", users=users, project=project, projects=projects)

#ROUTE CREATE NEW TASK INSIDE PROJECT
@projects_blueprint.route("/projects/<id>/tasks", methods=["POST"])
def create_task_in_project(id):
    user_id = request.form["user_id"]
    project_id = request.form["project_id"]
    title = request.form["title"]
    description = request.form["description"]
    user = user_repository.select(user_id)
    project = project_repository.select(project_id)
    new_task = Task(title, description, user, project)
    task_repository.save(new_task)
    return redirect(f"/projects/{id}/tasks")

#ROUTE UPDATE TASK INSIDE PROJECT
@projects_blueprint.route("/projects/<project_id>/tasks/<id>", methods=['POST'])
def update_task_in_project(project_id,id):
    title = request.form['title']
    description = request.form['description']
    user = user_repository.select(request.form['user_id'])
    project  = project_repository.select(request.form['project_id'])
    task = Task(title, description, user, project, False, id )
    task_repository.update(task)
    project = project_repository.select(project_id)
    return redirect(f"/projects/{project_id}/tasks", project = project)

#ROUTE EDIT TASK INSIDE PROJECT
@projects_blueprint.route("/projects/<project_id>/tasks/<id>/edit")
def edit_task_in_project(project_id,id):
    task = task_repository.select(id)
    project = project_repository.select(project_id)
    users = user_repository.select_all()
    projects = project_repository.select_all()
    task_repository.delete(id)
    return render_template('tasks/edit.html', task = task, projects = projects, users=users, project = project)

#ROUTE STATUS UPDATE INSIDE PROJECT
@projects_blueprint.route("/projects/<project_id>/tasks/<id>/status_update", methods=['POST'])
def status_update_task_in_project(project_id,id):
    task_to_edit = task_repository.select(id)
    completed = request.form['completed']
    task = Task(task_to_edit.title, task_to_edit.description, task_to_edit.user, task_to_edit.project, completed, id)
    task_repository.update(task)
    return redirect(f"/projects/{project_id}/tasks")

#ROUTE TASK DELETE INSIDE A PROJECT
@projects_blueprint.route("/projects/<project_id>/tasks/<id>/delete", methods=['POST'])
def delete_task(project_id,id):
    task_repository.delete(id)
    return redirect(f"/projects/{project_id}/tasks")

