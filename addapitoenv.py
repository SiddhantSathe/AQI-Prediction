import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional)
load_dotenv()

api_key = os.getenv("API_KEY_TIMEGPT")

if api_key is not None:
    print("API_KEY_TIMEGPT environment variable set")
    # ...
else:
    print("Error: API_KEY_TIMEGPT environment variable not set!")

# Set the environment
# try:
#     os.environ['API_KEY_OOO'] = 'a7814c89aa2e739b9b06a51ae2dccf6dc9d9ef18'
#     print('O3 environment variable set')
# except Exception as e:
#     print('Error O3 setting the environment variable:', e)
# try:
#     os.environ['API_KEY_TIMEGPT'] = 'nixtla-tok-ojwrR4rPpifERgb2RSrCjPx1Io6hh11YOmenD1ulLx8GogNe4AJHFwpK52kKpgMEedK7DcEAn8OlDOYV'
#     print('Timegpt environment variable set')
# except Exception as e:
#     print('Error timegpt setting the environment variable:', e)