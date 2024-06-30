# transfer data from csv to mysql database
import pandas as pd
import csv
import MySQLdb

# connect to mysql database
db = MySQLdb.connect(host="localhost", user="root", passwd="root@123", db="aqi")
cursor = db.cursor()

# real time data from api is in form of df in aqi.ipynb file
df = pd.read_csv('handle.csv')
df = df.drop('dew', axis=1)
df = df.dropna()
# print(df)

# # create table in mysql database
# cursor.execute('''
# CREATE TABLE aqi(
#     `index` INT AUTO_INCREMENT PRIMARY KEY,
#     city VARCHAR(50),
#     latitude FLOAT,
#     longitude FLOAT,
#     station VARCHAR(500),
#     dominant_pollutant VARCHAR(10),
#     timestamp DATETIME,
#     timestamp_timezone TIME,
#     aqi FLOAT,
#     AQI_meaning VARCHAR(50),
#     AQI_health_implications VARCHAR(500),
#     pm25 FLOAT,
#     pm10 FLOAT,
#     o3 FLOAT,
#     co FLOAT,
#     no2 FLOAT,
#     so2 FLOAT,
#     h FLOAT,
#     p FLOAT,
#     t FLOAT,
#     w FLOAT);
# ''')


# transfer data from csv to mysql database
# for i in range(len(df)):
#     cursor.execute('''
#     INSERT INTO aqi(`index`, city, latitude, longitude, station, dominant_pollutant, timestamp, timestamp_timezone, aqi, AQI_meaning, AQI_health_implications, pm25, pm10, o3, co, no2, so2, h, p, t, w)
#     VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     ''', (i, df['city'][i], df['latitude'][i], df['longitude'][i], df['station'][i], df['dominant_pollutant'][i], df['timestamp'][i], df['timestamp_timezone'][i], df['aqi'][i], df['AQI_meaning'][i], df['AQI_health_implications'][i], df['pm2.5'][i], df['pm10'][i], df['o3'][i], df['co'][i], df['no2'][i], df['so2'][i], df['h'][i], df['p'][i], df['t'][i], df['w'][i]))

# db.commit()
# cursor.close()
# db.close()
# print('Data transfered successfully')

def insert_aqi_data(df, connection):
  cursor = connection.cursor()

  for i in df.index:
    # Check if a record with the current index already exists
    check_query = "SELECT * FROM aqi WHERE `index` = %s"
    cursor.execute(check_query, (i,))

    # If a record exists, skip insertion (handle duplicate)
    if cursor.fetchone() is not None:
      print(f"Skipping record with index {i}. Duplicate detected.")
      continue

    # Insert data if no duplicate is found
    insert_query = """
      INSERT INTO aqi 
      (`index`, city, latitude, longitude, station, dominant_pollutant, timestamp, timestamp_timezone, aqi, AQI_meaning, AQI_health_implications, pm25, pm10, o3, co, no2, so2, h, p, t, w)
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (i, df['city'][i], df['latitude'][i], df['longitude'][i], df['station'][i], df['dominant_pollutant'][i], df['timestamp'][i], df['timestamp_timezone'][i], df['aqi'][i], df['AQI_meaning'][i], df['AQI_health_implications'][i], df['pm2.5'][i], df['pm10'][i], df['o3'][i], df['co'][i], df['no2'][i], df['so2'][i], df['h'][i], df['p'][i], df['t'][i], df['w'][i]))

  connection.commit()
  cursor.close()

# Assuming you have a connection object (`db`) established
insert_aqi_data(df, db)
print('Data transfered successfully (with duplicate handling)')


