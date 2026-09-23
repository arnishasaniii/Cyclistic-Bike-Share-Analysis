USE CyclisticDB;
GO

-- 1. Check Total Row Count (Should be ~5,547,380)
SELECT COUNT(*) AS total_records FROM Fact_Trips;

-- 2. Compare Member vs Casual Metrics
SELECT 
    member_casual,
    COUNT(*) AS total_trips,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage_share,
    ROUND(AVG(ride_length_min), 2) AS avg_ride_mins
FROM Fact_Trips
GROUP BY member_casual;