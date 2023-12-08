from werkzeug.utils import secure_filename
from flask import Flask, render_template, Blueprint, request
from flask_socketio import SocketIO, emit
import cv2
import math
from ultralytics import YOLO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'muhammadmoin'
socketio = SocketIO(app)
socketio.init_app(app, transports=['websocket', 'polling'])


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


def video_detection(path_x):
    video_capture = path_x

    cap = cv2.VideoCapture("../test/IMG_5957.MOV")
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    model = YOLO("../YOLO-Weights/best.pt")

    # classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    #               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    #               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    #               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    #               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
    #               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    #               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
    #               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
    #               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
    #               "teddy bear", "hair drier", "toothbrush"
    #               ]

    classNames = ["green","red"]

    while True:
        success, img = cap.read()
        results = model(img, stream=True)

        for r in results:
            data = []
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                #cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'

                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
                #data.append([x1, y1, x2, y2, label])
            #image
            # ref, buffer = cv2.imencode('.jpg', img)
            # frame = buffer.tobytes()
            # # YOLO 이미지를 전송
            # emit('yolo_frame', frame, broadcast=True)
            # # YOLO 결과 이미지와 변수들을 클라이언트로 전송
            # emit('yolo_result', data, broadcast=True)
            # test
            # emit('test','good',broadcast=True)
        out.write(img)
        cv2.imshow("Image",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('yolo_detection')
def handle_yolo_detection(path):
    path_x = 0
    video_detection(path_x)


# 이미지 받는 함수
# @socketio.on('orgin_image')
# def origin_image_yolo(image):
#     video_detection(image)
# @app.route("/ocr", methods=['POST'])
# def photo(img='https://user-images.githubusercontent.com/69428232/148330274-237d9b23-4a79-4416-8ef1-bb7b2b52edc4.jpg'):
#   print(ocr(img))
#   return ocr(img)


bp = Blueprint('image', __name__, url_prefix='/image')


# HTTP POST방식으로 전송된 이미지를 저장
@bp.route('/', methods=['POST'])
def save_image():
    f = request.files['file']
    f.save('./save_image/' + secure_filename(f.filename))
    return 'done!'


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
