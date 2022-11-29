from flask import Flask, render_template
from controllers.task_controller import tasks_blueprint
# from controllers.user_controller import users_blueprint
from controllers.project_controller import projects_blueprint
app = Flask(__name__)

app.register_blueprint(tasks_blueprint)
# app.register_blueprint(users_blueprint)
app.register_blueprint(projects_blueprint)

@app.route('/')
def home():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)