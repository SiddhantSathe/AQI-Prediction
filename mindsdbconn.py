import mindsdb_sdk
from mindsdb import Predictor
import pandas as pd


try:
    con = mindsdb_sdk.connect('http://127.0.0.1:47334')
    print('Connected to MindsDB')
except Exception as e:
    print('Error connecting to MindsDB:', e)
    con = None

# Assuming you have a CSV file with historical AQI and environmental data
data_path = 'historical_data.csv'

# Load your data into a pandas DataFrame
df = pd.read_csv(data_path)

# Define the column to predict (AQI in this case)
predictor = Predictor(name='aqi_predictor')
predictor.learn(
    from_data=df,
    to_predict='AQI'  # Replace 'AQI' with your target column name
)

# New data for prediction (future environmental data)
new_data = {
    'PM2.5': 15.3,
    'NO2': 0.9,
    'Temperature': 25.5,
    'Humidity': 60,
    'WindSpeed': 10
}

# Predict AQI for new data
result = predictor.predict(new_data)

print(f"Predicted AQI: {result['predicted_values']['AQI']}")












