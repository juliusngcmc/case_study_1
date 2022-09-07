import psycopg2
import csv
from config import config
import datetime
import time

def connect():
    """ Connect to the PostgresSQL database server """
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
        with open('sensor_value.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row.
            for row in reader:
                # Temperature on a normal scale (2000 means 20)
                if row[2] == "Temperature":
                    row[3] = int(row[3])/100
                # Ignore Humidity value that is negative or greater than 100
                if row[2] == "Humidity" and (int(row[3]) > 100 or int(row[3]) < 0):
                    continue
                # Use the integral Unix time instead of the ISO 8601 timestamp
                time_temp = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
                row[1] = time.mktime(time_temp.timetuple())
                # Insert data value to sensor_value table
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


if __name__ == '__main__':
    connect()
