from flask import Flask, jsonify, request, render_template, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypass@localhost:5431/postgres'
# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)


class Books(db.Model):
    __tablename__ = 'books'
    book_title = db.Column(db.String(100), primary_key=True)
    book_text = db.Column(db.String(), nullable=False)
    likes = db.Column(db.Integer(), nullable=False, default=0)

    def __init__(self, book_title, book_text, likes):
        self.book_title = book_title
        self.book_text = book_text
        self.likes = likes


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


@app.route('/test', methods=['GET'])
def test():
    return {
        'test': 'test1'
    }


@app.route('/get_books', methods=['GET'])
def getbooks():
    all_books = Books.query.all()
    output = []
    for book in all_books:
        curr_book = {}
        curr_book['book_title'] = book.book_title
        curr_book['book_text'] = book.book_text
        curr_book['likes'] = book.likes
        output.append(curr_book)
    return jsonify(output)


@app.route('/post_books', methods=['POST'])
def postbook():
    book_data = request.get_json()
    book = Books(book_title=book_data['book_title'], book_text=book_data['book_text'], likes=book_data['likes'])
    db.session.add(book)
    db.session.commit()
    return jsonify(book_data)


# $env:FLASK_APP="flask_test.py"


if __name__ == "__main__":
    app.run(port=5000)
