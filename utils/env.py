import os 
from dotenv import load_dotenv

load_dotenv(override=True)

class Env:
    # BASE_URL = os.getenv("BASE_URL")
    API_BASE_URL = os.getenv("API_BASE_URL")