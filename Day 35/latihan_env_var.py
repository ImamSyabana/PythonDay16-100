import os
from dotenv import find_dotenv, load_dotenv

# mencari lokasi file .env secara otomatis 
dotenv_path = find_dotenv()

# load the entries as environtment variables
load_dotenv(dotenv_path)

# stored the env variables within a python variable
API_KEY = os.getenv("API_KEY")

print(API_KEY)
