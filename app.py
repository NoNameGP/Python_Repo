from flask import Flask
from flask_migrate import Migrate
from models.model import db,login_manager
from routes.route import Route


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app


app = create_app()
Route(app)
migrate = Migrate(app, db)
login_manager.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
