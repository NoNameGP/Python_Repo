from flask import Flask, render_template
from flask_migrate import Migrate
from models.model import db, login_manager
from routes.route import Route
from controllers.controller import socketio, YoloController


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    return app


app = create_app()
Route(app)
migrate = Migrate(app, db)
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('yolo_detection')
def handle_yolo_detection(path):
    controller = YoloController()
    controller.video_detection()


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
