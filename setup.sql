create table public.sersor_value
(
    sensor_id serial primary key,
    timestamp TIMESTAMP NOT NULL,
    sensor_type VARCHAR ( 50 ) NOT NULL,
    reading INT NOT NULL
)

