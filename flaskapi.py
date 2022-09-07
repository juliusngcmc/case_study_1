from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
import csv
from config import config

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
        # Connect to the PostgresSQL database server
        conn = None
        try:
            # read connection parameters
            params = config()
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            # create a cursor
            cur = conn.cursor()
            # execute a statement
            with open('input_sensor_data/sensor_value.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row.
                for row in reader:
                    cur.execute(
                        "INSERT INTO sensor_value VALUES (%s, %s, %s, %s)",
                        row
                    )
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(port=5000)
