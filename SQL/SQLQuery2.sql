USE CyclisticDB;
GO

BULK INSERT Fact_Trips
FROM 'C:\Users\Admin\OneDrive\Desktop\Google Case Study\01_Clean_Data\cyclistic_clean_trips.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);