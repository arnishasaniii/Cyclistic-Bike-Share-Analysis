import pandas as pd
import glob
import os

# Identify paths relative to project root
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
project_root = os.path.dirname(script_dir) if "02_Scripts" in script_dir else script_dir

raw_data_path = os.path.join(project_root, "00_Raw_Data", "*.csv")
output_dir = os.path.join(project_root, "01_Clean_Data")

# 1. Combine all 12 CSV files
all_files = glob.glob(raw_data_path)
print(f"Found {len(all_files)} files in 00_Raw_Data. Loading and combining...")

df_list = [pd.read_csv(file) for file in all_files]
df = pd.concat(df_list, ignore_index=True)
print(f"Total Raw Rows: {len(df):,}")

# 2. Datetime Conversion
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# 3. Feature Engineering
df['ride_length_min'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60.0
df['day_of_week'] = df['started_at'].dt.day_name()
df['month'] = df['started_at'].dt.month_name()
df['hour'] = df['started_at'].dt.hour

# 4. Data Cleaning (remove <=0 duration and >24h rides)
df_clean = df[(df['ride_length_min'] > 0) & (df['ride_length_min'] <= 1440)].copy()
df_clean['member_casual'] = df_clean['member_casual'].str.lower().str.strip()

print(f"Total Cleaned Rows: {len(df_clean):,}")
print(f"Removed Invalid Records: {len(df) - len(df_clean):,}")

# 5. Export clean dataset
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "cyclistic_clean_trips.csv")
df_clean.to_csv(output_file, index=False)
print(f"\nSuccess! Cleaned dataset saved to: {output_file}")