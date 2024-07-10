from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import ozon3 as ooo
import mindsdb_sdk


app = Flask(__name__)

#o3 api connection
o3 = ooo.Ozon3('a7814c89aa2e739b9b06a51ae2dccf6dc9d9ef18')

# connect to mindsdb
server = mindsdb_sdk.connect()

# def predict_aqi():
#     city = input('Enter city name: ')
#     city = o3.get_city_forecast(city)
#     aqi = 0
#     for i in ['pm2.5', 'o3', 'pm10']:
#         aqi += city[i]
#     aqi = aqi/3
#     return aqi

# store data from api connection to mindsdb

def store_data():
    #create a new database
    db = server.create_database('aqi')
    #create a new table
    table = db.create_table('aqi_data')
    #add columns
    table.add_column('city', mindsdb_sdk.STRING)
    table.add_column('latitude', mindsdb_sdk.FLOAT)
    table.add_column('longitude', mindsdb_sdk.FLOAT)
    table.add_column('station', mindsdb_sdk.STRING)
    table.add_column('dominant_pollutant', mindsdb_sdk.STRING)
    table.add_column('timestamp', mindsdb_sdk.DATETIME)
    table.add_column('timestamp_timezone', mindsdb_sdk.TIME)
    table.add_column('avg_aqi', mindsdb_sdk.FLOAT)
    table.add_column('min_aqi', mindsdb_sdk.FLOAT)
    table.add_column('max_aqi', mindsdb_sdk.FLOAT)
    table.add_column('AQI_meaning', mindsdb_sdk.STRING)
    table.add_column('AQI_health_implications', mindsdb_sdk.STRING)
    table.add_column('forecasted_pm25', mindsdb_sdk.FLOAT)
    table.add_column('forecasted_pm10', mindsdb_sdk.FLOAT)
    table.add_column('forecasted_o3', mindsdb_sdk.FLOAT)

    #insert data
    city = input('Enter city name: ')
    city = o3.get_city_forecast(city)
    table.insert(city)
    
