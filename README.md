Cyclistic Bike-Share Case Study
Google Data Analytics Capstone Project
Author: Arnis Hasani
Tools: Python | SQL Server | Power BI

Project Overview
Cyclistic is a bike-share company in Chicago with over 5,800 bicycles and 600 stations. The marketing team wants to get more annual members because members bring in more steady revenue than casual riders.

As a data analyst, my job was to look at 12 months of trip data (over 5.5 million rows) to see how annual members and casual riders use the bikes differently. Based on those patterns, I came up with simple recommendations to help convert casual riders into annual members.

The Main Question
How do annual members and casual riders use Cyclistic bikes differently, and how can we use those differences to convince casual riders to buy a membership?

Tools Used

Python: Used to combine 12 separate CSV files into one dataset, remove bad data (like negative ride times), and add new fields for analysis.

SQL Server (SSMS): Used to store the clean data and run queries to calculate trip counts, average ride lengths, and peak usage hours.

Power BI: Used to build an interactive dashboard with simple visual charts for stakeholders.

Key Findings

Total Volume: Annual members make up 64% of total trips, while casual riders account for 36%.

Trip Length: Casual riders ride for longer periods, averaging 19.1 minutes per trip compared to 12.0 minutes for members.

Weekly Pattern: Members ride mostly Monday through Friday for work commutes. Casual riders peak on Saturday and Sunday for leisure.

Hourly Pattern: Members show clear spikes at 8 AM and 5 PM rush hours. Casual trips grow steadily throughout the day and peak in the late afternoon.

Seasonality: Casual riding surges in the summer and drops off heavily in the winter, while member riding stays more consistent year-round.

Dashboard Preview

Recommendations

Weekend and Summer Promotions: Offer casual riders unlocking bikes on summer weekends a special discount or credit toward an annual membership.

Commuter Trial Pass: Target casual riders who unlock bikes during weekday rush hours (8 AM and 5 PM) with a discounted one-month trial pass.

Ride Time Rewards: Give casual riders points for total minutes ridden, which they can convert into money off an annual pass.

Project Structure
Google-Case-Study/

00_Raw_Data/ (12 raw monthly CSV files)

01_Clean_Data/ (combined clean dataset)

02_Scripts/01_clean_data.py (Python script)

03_SQL/01_analysis.sql (SQL analysis script)

04_PowerBI/Dashboard.pbix (Power BI file)

04_PowerBI/dashboard_preview.png (dashboard image)

.gitignore (keeps large dataset files off GitHub)

README.md (project overview)

How to Run

Run the script in 02_Scripts/01_clean_data.py to clean and combine the raw data.

Run the queries in 03_SQL/01_analysis.sql in SQL Server Management Studio.

Open 04_PowerBI/Dashboard.pbix in Power BI Desktop to view the interactive dashboard.