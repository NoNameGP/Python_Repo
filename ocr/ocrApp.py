from flask import Flask, Blueprint, request
from werkzeug.utils import secure_filename
from ocr import ocr

app = Flask(__name__)

img = 'https://user-images.githubusercontent.com/69428232/148330274-237d9b23-4a79-4416-8ef1-bb7b2b52edc4.jpg'


@app.route("/ocr", methods=['GET', 'POST'])
def photo(img='https://user-images.githubusercontent.com/69428232/148330274-237d9b23-4a79-4416-8ef1-bb7b2b52edc4.jpg'):
    print(ocr(img))
    return ocr(img)


bp = Blueprint('image', __name__, url_prefix='/image')


# HTTP POST방식으로 전송된 이미지를 저장
@bp.route('/', methods=['POST'])
def save_image():
    f = request.files['file']
    f.save('./save_image/' + secure_filename(f.filename))
    return 'done!'

if __name__ == '__main__':
    app.run(debug=True)

