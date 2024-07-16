import mindsdb_sdk
import os
from dotenv import load_dotenv
import ozon3 as ooo


load_dotenv()

o3 = ooo.Ozon3(os.environ['API_KEY_OOO'])
server = mindsdb_sdk.connect()


def get_aqi_predictions(project= server.get_project('aqi'), limit=10):
    query = f"""
    SELECT m.date, m.`pm2.5` AS predicted_pm25, t.`pm2.5` AS actual_pm25 
    FROM files.historic_houston t 
    JOIN aqi_forecast_nixtla m
    WHERE t.date > LATEST
    LIMIT {limit}
    """
    return project.query(query)