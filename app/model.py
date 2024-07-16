import mindsdb_sdk
import os
from dotenv import load_dotenv
import ozon3 as ooo


load_dotenv()

o3 = ooo.Ozon3(os.environ['API_KEY_OOO'])
server = mindsdb_sdk.connect()


def create_model():
    project = server.get_project('aqi')
    try:
      model = project.models.create(
    name='aqi_forecast_model',
    predict='`pm2.5`',
    query='SELECT * FROM files.historic_houston',
    timeseries_options={
        'order': 'date',
        'horizon': 5
    },
    engine='timegpt',
    timegpt_api_key='nixtla-tok-ojwrR4rPpifERgb2RSrCjPx1Io6hh11YOmenD1ulLx8GogNe4AJHFwpK52kKpgMEedK7DcEAn8OlDOYV'
)
      print('Model created')
    except Exception as e:
        model = project.models.get('aqi_forecast_model')
        print('Error creating model:', e)
    return model

# def data_cleaning():
#     data = o3.get_city_air('Mumbai')
#     # if nan then remove that column
#     data = data.dropna(how='any', axis=1)
#     return data

# def add_data():
#     data = data_cleaning()
#     try:
#         files_db = server.get_database('files')
#         files_db.create_table('aqi_file', data)
#         print('Data added')
#     except:
#         table = files_db.get_table('aqi_file')
#         print('file table already exists')
        
    
# def create_models():
#     try:
#         project = server.get_project('aqi')
#     except:
#         project = server.create_project('aqi')

    # try:
    #     model = project.models.get('aqi_forecast_nixtla')
    #     print('Model "aqi_forecast_nixtla" found')
    # except Exception as e:
    #     print(f"Model not found: {e}")
    
    # try:
    #     timegpt_api = {'timegpt':os.environ['API_KEY_TIMEGPT']}
    #     print('Timegpt environment variable set')
    # except Exception as e:
    #     print('Error timegpt setting the environment variable:', e)

    # try:
    #     description = model.describe()
    #     print(description)
    # except Exception as e:
    #     print(f"Error describing model: {e}")

    # try:
    #     data = data_cleaning()
    #     my_table = project.tables.create('aqi_data', data)
    #     print('Table created')
    # except Exception as e:
    #     print(f"Error creating table: {e}")




    # try:
#         model = project.models.create(
#     name='aqi_forecast_model',
#     predict='aqi',
#     query='SELECT date, city, dominant_pollutant, aqi FROM aqi_data',
#     timeseries_options={
#         'order': 'date',
#         'group': ['city', 'dominant_pollutant'],
#         'horizon': 7
#     },
#     engine='timegpt',
#     timegpt_api_key=os.environ['API_KEY_TIMEGPT']
# )
#         model = project.models.create(
#     name='aqi_forecast_model',
#     query='SELECT timestamp AS ds, city, dominant_pollutant, aqi AS y FROM files.handled_data',
#     predict='y',
#     timeseries_options={
#         'order': 'ds',
#         'group': ['city', 'dominant_pollutant'],
#         'horizon': 7
#     },
#     engine='timegpt',
#     timegpt_api_key=os.environ['API_KEY_TIMEGPT']
# )
#         print('Model created')
#     except Exception as e:
#         # print(f"Error creating model: {e}")
#         model = project.models.get('aqi_forecast_model')
#         print('Model found')


    #ensure that the model is trained
    # try:
    #     model.train()
    #     print('Model trained')
    # except Exception as e:
    #     print(f"Error training model: {e}")

# Make predictions

#     try:
#         model.predict({
#     "ds": "2024-06-30 13:00:00",
#     "city": "Mumbai",
#     "dominant_pollutant": "pm2.5"
# })
#         print('Predictions made successfully')
#     except Exception as e:
#         print(f"Error predicting: {e}")
    # try:
    #     predictions = model.predict(data)
    #     print(predictions)
    # except Exception as e:
    #     print(f"Error predicting: {e}")

