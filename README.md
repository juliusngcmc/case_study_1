# I. Summary of case study
[Click here](https://yuthefirst.notion.site/Case-Study-1-Sensor-data-pipeline-using-PostgreSQL-and-Python-based-RESTful-APIs-d723db8cf77047ccb77cc63f8afe5bce)

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
![alt text](https://github.com/juliusngcmc/case_study_1/blob/main/readme_image/img.png?raw=true)
