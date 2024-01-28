from flask import Flask, render_template
from flask_migrate import Migrate
from models.model import db, login_manager
from routes.route import Route

from flask_socketio import SocketIO, emit
import cv2
import math
from ultralytics import YOLO


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app


app = create_app()
route = Route(app)
migrate = Migrate(app, db)
login_manager.init_app(app)

socketio = SocketIO(app)
# socketio.init_app(app, transports=['websocket', 'polling'])


class ClassNames:
    coco = ['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
            'fire hydrant', 'stop sign', 'parking meter',
            'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra',
            'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',
            'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
            'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon',
            'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
            'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor',
            'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink',
            'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

    best = ["green", "red"]


class YOLOService:
    def process_video_detection(self, results, class_names):

        global class_name

        for r in results:
            data = []
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                if cls in [0, 1, 2, 3, 5, 7, 9]:
                    class_name = class_names[cls]
                    data.append([x1, y1, x2, y2, class_name, conf])

            # # YOLO 결과 변수들을 클라이언트로 전송
            emit('yolo_result', data)


class YOLOController:

    path = "../YOLO-Weights/"

    def __init__(self, model="best.pt"):
        self.cap = cv2.VideoCapture(0)
        self.model = YOLO(self.path+model)
        self.class_names = ClassNames.best if model == "best.pt" else ClassNames.coco

    def video_detection(self):
        while True:
            success, img = self.cap.read()
            results = self.model(img, stream=True)

            YOLOService().process_video_detection(results, self.class_names)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # STOP API 만들기
                break
        self.cap.release()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('yolo_detection')
def handle_yolo_detection(path):
    YOLOController(path).video_detection()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
