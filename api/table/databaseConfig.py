from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'jdbc:mysql://localhost:3306/dukjins'
app.config['SQLALCHEMY_TRACK_MODIFICATTIONS'] = False