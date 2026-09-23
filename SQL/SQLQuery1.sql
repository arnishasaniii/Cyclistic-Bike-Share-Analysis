-- 1. Create the Cyclistic Database
CREATE DATABASE CyclisticDB;
GO

USE CyclisticDB;
GO

-- 2. Create the target table schema
CREATE TABLE Fact_Trips (
    ride_id VARCHAR(50),
    rideable_type VARCHAR(50),
    started_at DATETIME2,
    ended_at DATETIME2,
    start_station_name VARCHAR(255),
    start_station_id VARCHAR(100),
    end_station_name VARCHAR(255),
    end_station_id VARCHAR(100),
    start_lat FLOAT,
    start_lng FLOAT,
    end_lat FLOAT,
    end_lng FLOAT,
    member_casual VARCHAR(20),
    ride_length_min FLOAT,
    day_of_week VARCHAR(20),
    month VARCHAR(20),
    hour INT
);