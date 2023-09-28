from flask import Flask, render_template
from flask_migrate import Migrate
from server import create_app, db

app = create_app()

migrate = Migrate(app,db)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
