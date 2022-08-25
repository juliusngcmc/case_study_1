from peewee import *
import config

database = PostgresqlDatabase(
    user=config.DATABASES['USER'],
    password=config.DATABASES['PASSWORD'],
    database=config.DATABASES['NAME'],
    host=config.DATABASES['HOST'],
    port=config.DATABASES['PORT']
)


class BaseModel(Model):
    class Meta:
        database = database


# Creating a Sensor EndOfDay Value
class SensorEODValue(BaseModel):
    sensor_id = AutoField()
    timestamp = DateTimeField()
    sensor_type = CharField(max_length=15)
    reading = DecimalField(max_digits=14, decimal_places=7)
    created_date = DateTimeField(constraints=[SQL("Default now()")], null=False)

    class Meta:
        table_name = 'sensor_value'
