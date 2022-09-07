from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'input_sensor_data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Root URL
@app.route('/')
def index():
    # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Get the uploaded files
@app.route("/", methods=['POST'])
def upload_files():
    # get the uploaded file
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        # save the file
        return redirect(url_for('index'))


# Unable track modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Connect to PostgreSQL Server
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypass@localhost:5431/postgres'
db = SQLAlchemy(app)


class SensorValue(db.Model):
    __tablename__ = 'books'
    sensor_id = db.Column(db.SERIAL(), primary_key=True)
    timestamp = db.Column(db.TIMESTAMP(), nullable=False)
    sensor_type = db.Column(db.VARCHAR(), nullable=False, default=0)
    reading = db.Column(db.INTEGER(), nullable=False, default=0)

    def __init__(self, book_title, book_text, likes):
        self.book_title = book_title
        self.book_text = book_text
        self.likes = likes


if __name__ == "__main__":
    app.run(port=5000)
