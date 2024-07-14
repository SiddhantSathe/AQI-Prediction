import mindsdb_sdk
import os
from dotenv import load_dotenv

load_dotenv()

def create_models():
    server = mindsdb_sdk.connect()
    try:
        project = server.get_project('aqi')
    except:
        project = server.create_project('aqi')

    try:
        model = project.models.get('aqi_forecast_nixtla')
        print('Model "aqi_forecast_nixtla" found')
    except Exception as e:
        print(f"Model not found: {e}")
    
    try:
        timegpt_api = {'timegpt':os.environ['API_KEY_TIMEGPT']}
        print('Timegpt environment variable set')
    except Exception as e:
        print('Error timegpt setting the environment variable:', e)

    try:
        prediction = model.predict({"date": '2024-07-04'})
        print(prediction)
    except Exception as e:
        print(f"Error predicting: {e}")


create_models()