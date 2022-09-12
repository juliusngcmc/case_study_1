DROP VIEW IF EXISTS sensor_temperature_view;
DROP VIEW IF EXISTS hourly_median_temperature_view;
DROP VIEW IF EXISTS dew_point_view;
DROP VIEW IF EXISTS only_temp_view;
DROP VIEW IF EXISTS only_humid_view;

CREATE VIEW hourly_median_temperature_view AS
SELECT sensor_id, sensor_type,
       date_trunc('hour', to_timestamp(timestamp)) as time, --Switch timestamp from Unix to ISO 8601
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY reading ) AS hourly_median_temperature --Calculate the hourly median temperature
FROM sensor_value
where sensor_type like 'Temperature'
group by sensor_id, time, sensor_type
order by sensor_id;

CREATE VIEW sensor_temperature_view AS
SELECT sensor_id, sensor_type, time, hourly_median_temperature,
       ROUND(CAST((hourly_median_temperature - (LAG(hourly_median_temperature) OVER (ORDER BY sensor_id)))/
       (LAG(hourly_median_temperature) OVER (ORDER BY sensor_id))*100.00 AS numeric),2) as percentage_difference
FROM hourly_median_temperature_view
group by sensor_id, sensor_type, time, hourly_median_temperature
order by sensor_id;

-------------------------------------------------------------------------------------

CREATE VIEW only_temp_view AS
SELECT sensor_id, sensor_type,
       date_trunc('hour', to_timestamp(timestamp)) as time, --Switch timestamp from Unix to ISO 8601
       (extract(minute FROM (to_timestamp(timestamp)))::int / 30) AS min30_slot,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY reading ) AS temp_reading --Calculate the hourly median temperature
FROM sensor_value
where sensor_type like 'Temperature'
group by sensor_id, time, sensor_type, min30_slot
order by sensor_id;

CREATE VIEW only_humid_view AS
SELECT sensor_id, sensor_type,
       date_trunc('hour', to_timestamp(timestamp)) as time, --Switch timestamp from Unix to ISO 8601
       (extract(minute FROM (to_timestamp(timestamp)))::int / 30) AS min30_slot,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY reading ) AS humid_reading --Calculate the hourly median temperature
FROM sensor_value
where sensor_type like 'Humidity'
group by sensor_id, time, sensor_type, min30_slot
order by sensor_id;

CREATE VIEW dew_point_view AS
SELECT only_humid_view.sensor_id,
       case when only_humid_view.min30_slot = 1
           then only_humid_view.time + interval '30' minute
           else only_humid_view.time end as times,
       only_temp_view.temp_reading as T,
       only_humid_view.humid_reading as RH,
       only_temp_view.temp_reading + (only_humid_view.humid_reading-100)/5 as dew_point
FROM only_temp_view
INNER JOIN only_humid_view ON
    only_temp_view.sensor_id = only_humid_view.sensor_id and
    only_temp_view.time = only_humid_view.time and
    only_temp_view.min30_slot = only_humid_view.min30_slot;
