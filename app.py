from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import ozon3 as ooo
import mindsdb_sdk
import os
import dotenv
from app.model import create_model
from app.query import get_aqi_predictions

model_instance = create_model()
query_instance = get_aqi_predictions()

dotenv.load_dotenv()


app = Flask(__name__)
CORS(app)

#o3 api connection
o3 = ooo.Ozon3(os.environ['API_KEY_OOO'])

# connect to mindsdb
try:
    server = mindsdb_sdk.connect()
    print('Connected to MindsDB')
except Exception as e:
    print('Connection to MindsDB failed: ', e)

try:
  project = server.get_project('aqi')
  print('Project "aqi" found')
except Exception as e:
    project = server.create_project('aqi')
    print('Model aqi created and error:', e)
    
    

@app.route('/search', methods=['POST'])

def handle_request():
    data = request.json
    city = data.get('city')
    data = o3.get_city_air(city)
    # Assuming 'aqi' is a column in your DataFrame
    aqi_value = data['aqi'].iloc[0]  # This gets the first 'aqi' value; adjust as needed
    return jsonify(aqi=aqi_value)

def get_data():
    data = request.json
    city = data.get('city')
    data = o3.get_historical_data(city= city)
    data = data.dropna()
    return data

# def add_data():
#     data = get_data()
#     try:
#         files_db = server.get_database('files')
#         files_db.create_table('city_data', data)
#         print('Data added')
#     except:
#         table = files_db.get_table('city_data')
#         print('file table already exists')
#     return table

@app.route('/add_data', methods=['POST'])
def add_data_route():
    city = request.json.get('city')
    data = o3.get_historical_data(city=city)
    data = data.dropna()
    try:
        files_db = server.get_database('files')
        files_db.create_table('city_data', data)
        print('Data added')
    except Exception as e:
        table = files_db.get_table('city_data')
        print('file table already exists', e)
    return "Data processing complete"


@app.route('/create_model', methods=['GET'])
def create_model_route():
    try:
        model = model_instance  # Call the create_model function
        return jsonify({'message': 'Model created successfully'}), 200  # Assuming the model object has an 'id' attribute
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# @app.route('/get_aqi_predictions', methods=['GET'])

# def get_aqi_predictions(project= server.get_project('aqi'), limit=10):
#     query = f"""
#     SELECT m.date, m.`pm2.5` AS predicted_pm25, t.`pm2.5` AS actual_pm25 
#     FROM files.historic_houston t 
#     JOIN aqi_forecast_nixtla m
#     WHERE t.date > LATEST
#     LIMIT {limit}
#     """
#     return project.query(query)

@app.route('/get_aqi_data', methods=['GET'])
def get_aqi_data():
    project = server.get_project('aqi')
    results = get_aqi_predictions(project)
    df = results.fetch()  # Assuming this returns a pandas DataFrame

    filtered_df = df[['date', 'predicted_pm25']]

    # Convert the DataFrame to a JSON object
    df_json = filtered_df.to_json(orient='records')
    
    # Return the JSON data
    return jsonify(df_json)


# project = server.get_project('aqi')

# results = get_aqi_predictions(project)
# df = results.fetch()



# def get_aqi_predictions(project, limit=10):
#     query = f"""
#     SELECT m.date, m.`pm2.5` AS predicted_pm25, t.`pm2.5` AS actual_pm25 
#     FROM files.city_data t 
#     JOIN aqi_forecast_nixtla m
#     WHERE t.date > LATEST
#     LIMIT {limit}
#     """
#     return project.query(query)

# project = server.get_project('aqi')

# results = get_aqi_predictions(project)
# df = results.fetch()

# print(df)


if __name__ == '__main__':
    app.run(debug=True)