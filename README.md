Cyclistic Bike-Share Analysis
Google Data Analytics Capstone Project
Author: Arnis Hasani
Tools: Python · SQL Server · Power BI


What is this project?

This is my capstone project for the Google Data Analytics Certificate.

Cyclistic is a bike-share company in Chicago with 5,800 bikes and 600 stations.
The business problem is simple — casual riders are less profitable than annual members
and the marketing team wants to convert them.

I went beyond the basic requirements. Instead of using a sample I processed the full
12 months of trip data — over 5.5 million rows. I built a Python cleaning pipeline,
stored everything in SQL Server, and built a Power BI dashboard for the final presentation.


The question I was answering

How do annual members and casual riders use the bikes differently — and what does
that tell us about how to convert casuals into members?


What I did

Python — combined 12 separate monthly CSV files into one dataset, removed bad data
like negative ride times, and added calculated fields for analysis.

SQL Server — stored the clean data and ran queries to calculate trip counts,
average ride lengths, and peak usage hours by rider type.

Power BI — built an interactive dashboard to present the findings.


What I found

Members make up 64% of total trips, casuals 36%.

Casual riders average 19.1 minutes per trip vs 12 minutes for members.
They ride longer but commit less — price or habit is the barrier, not interest.

Members ride Monday to Friday for commuting. Casuals peak Saturday and Sunday for leisure.
These are two completely different use cases in the same product.

Members show clear spikes at 8 AM and 5 PM. Casual usage builds slowly through the day.

Casual riding drops heavily in winter while member riding stays consistent year-round.
Seasonality is a major factor for this segment.


What I would recommend to the business

Target casual riders who already use bikes during weekday rush hours — they are
behaving like members without the membership. A one month discounted trial pass
aimed at this group would convert the easiest wins first.

Run summer weekend promotions specifically — that is when casual volume is highest
and willingness to engage is strongest.

Add a ride time rewards system — casuals ride longer so they accumulate points faster.
Give them something to unlock and they have a reason to come back.


Project structure

00_Raw_Data — 12 raw monthly CSV files
01_Clean_Data — combined clean dataset
02_Scripts — Python cleaning script
SQL — SQL analysis queries
03_PowerBI — Power BI dashboard file and preview


Tools
Python, pandas, SQL Server, Power BI
Dataset: Cyclistic trip data — 12 months, 5.5 million rows
