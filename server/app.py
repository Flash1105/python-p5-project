from flask import Flask, render_template
from flask_migrate import Migrate
from server.config import Config
from .database import db, init_app

app = Flask(__name__, template_folder='../templates')
app.config.from_object(Config)

init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
