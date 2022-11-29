import pdb

from models.task import Task
import repositories.task_repository as task_repository

from models.user import User
import repositories.user_repository as user_repository

from models.project import Project
import repositories.project_repository as project_repository


# biting_repository.delete_all()
task_repository.delete_all()
project_repository.delete_all()
user_repository.delete_all()

user_1 = User('George')
user_2 = User('Alex')
project_1 = Project('"Trenello" Solo Project')
project_2 = Project('Week 13 Team Project')
task_1 = Task('Wireframe','Create wireframe of the app', user_1, project_1)
task_2 = Task('Class and Object Diagrams','Create class and object relational diagrams', user_1, project_1)
task_3 = Task('Database','Initiate a database', user_1, project_1)
task_4 = Task('Team meeting','Organise a team meeting to discuss project', user_1, project_2)
task_5 = Task('Presentation','Create a presentation', user_1, project_2)

user_repository.save(user_1)
user_repository.save(user_2)
project_repository.save(project_1)
project_repository.save(project_2)
task_repository.save(task_1)
task_repository.save(task_2)
task_repository.save(task_3)
task_repository.save(task_4)
task_repository.save(task_5)


pdb.set_trace()
