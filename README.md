# I. Summary of case study
[Click here](https://yuthefirst.notion.site/Case-Study-1-Sensor-data-pipeline-using-PostgreSQL-and-Python-based-RESTful-APIs-d723db8cf77047ccb77cc63f8afe5bce) to see all requirements of this case study.

# II. Running step by step
- Step 1: Create an enviroment and activate and enviroment
```
python -m venv env
```
```
.\env\Scripts\activate"
```
- Step 2: Install docker and needed library 
```
pip install -r requirements.txt
```
- Step 3: Running a PostgreSQL server on docker
```
docker-compose up -d
```
- Step 4: Connect to PostgreSQL server that we have just created by any IDE. In my case, I use database function on Pycharm.
Host: localhost
Port: 5431
User: postgres
Passward: mypass
Database: postgres

![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img.png?raw=true)

- Step 5: Run Python REST API:
```
python .\flaskapi.py 
```
Then click on link appear on terminal. Usually is running on [http://127.0.0.1:5000](http://127.0.0.1:5000).
Browser will appear like this
![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img_1.png?raw=true)

Press Ctrl + C to exit the REST API running.
- Step 6: 
Click Choose File to choose a csv file to PostgreSQL Server. We can using [this](https://github.com/juliusngcmc/case_study_1/blob/main/sensor_value.csv) in the repo as an input demo. Then hit submit. The CSV will be insert in PostgreSQL Server
If you choose another csv file, please stay with this format.
  - The name of CSV file is "sensor_value.csv"
  - The column name of CSV file arranged in order: sensor_id, timestamp, sensor_type, reading

- Step 7:
For the "usiness Requirements", running the [bussiness_requirement.sql](https://github.com/juliusngcmc/case_study_1/blob/main/bussiness_requirement.sql) to create a view for:
  - The hourly median temperature for each sensor (hourly_median_temperature_view)
  - The percentage difference in hourly average temperature against the previous hour for each sensor (sensor_temperature_view)
  - The half-hourly average “dew point” for each sensor (dew_point_view)
