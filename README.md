# I. Summary of case study
[Click here](https://yuthefirst.notion.site/Case-Study-1-Sensor-data-pipeline-using-PostgreSQL-and-Python-based-RESTful-APIs-d723db8cf77047ccb77cc63f8afe5bce) to see all requirements of this case study.

# II. Running step by step
## Step 1: Create an enviroment and activate and enviroment
```
python -m venv env
```
```
.\env\Scripts\activate
```
## Step 2: Install docker and needed library 
```
pip install -r requirements.txt
```
```
pip install docker
```
## Step 3: Running a PostgreSQL server on docker
```
docker-compose up -d
```
## Step 4: Connect to PostgreSQL server that we have just created by any IDE. In my case, I use database function on Pycharm.
  - Host: localhost
  - Port: 5431
  - User: postgres
  - Passward: mypass
  - Database: postgres

![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img.png?raw=true)

## Step 5: Run Python REST API:
```
python .\flaskapi.py 
```
Then click on link appear on terminal. Usually is running on [http://127.0.0.1:5000](http://127.0.0.1:5000).
Browser will appear like this
![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img_1.png?raw=true)

Press Ctrl + C to exit the REST API running.
## Step 6: 
Click Choose File to choose a csv file to PostgreSQL Server. We can using [this](https://github.com/juliusngcmc/case_study_1/blob/main/sensor_value.csv) in the repo as an input demo. Then hit submit. The CSV will be insert in PostgreSQL Server.
If you choose another csv file, please stay with this format.
  - The name of CSV file is "sensor_value.csv"
  - The column name of CSV file arranged in order: sensor_id, timestamp, sensor_type, reading
![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img_2.png?raw=true)

## Step 7:
Using Pyspark to transform data with Business Requirements. Open the log of Pyspark to access Jupyter Notebook via "http://127.0.0.1:8888/lab?token..."
![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img_6.png?raw=true)
### NOTE: Run this command first on Jupiter-Notebook Terminal!
```
pyspark --jars postgresql.jar
```
![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img_9.png?raw=true) 
Then open the run.ipynb in work folder. Then chose Run => Run All Cells                                                                                    
![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img_7.png?raw=true)                                                     
The notebook will create the dew_point.csv
![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img_8.png?raw=true)
