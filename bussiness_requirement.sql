CREATE VIEW sensor_value_view AS
SELECT sensor_id, sensor_type,
       date_trunc('hour', to_timestamp(timestamp)) as time, --Switch timestamp from Unix to ISO 8601
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY reading ) AS hourly_median_temperature --Calculate the hourly median temperature
FROM sensor_value
where sensor_type like 'Temperature'
group by sensor_id, time, sensor_type, reading
order by sensor_id;