class Task:
    def __init__(self, title, description, user, project, completed=False,  id=None):
        self.title = title
        self.description = description
        self.user = user
        self.project = project
        self.completed = completed
        self.id = id