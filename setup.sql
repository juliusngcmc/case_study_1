create table public.sensor_value
(
    sensor_id INT NOT NULL,
    timestamp BIGINT NOT NULL,
    sensor_type VARCHAR ( 50 ) NOT NULL,
    reading INT NOT NULL
)

