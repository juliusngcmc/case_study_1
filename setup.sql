create table public.sensor_value
(
    sensor_id INT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    sensor_type VARCHAR ( 50 ) NOT NULL,
    reading INT NOT NULL
)

