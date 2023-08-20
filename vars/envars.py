import os
from dotenv import load_dotenv

load_dotenv()
SERVICE_BASE_URL = os.environ['SERVICE_BASE_URL']
SERVICE_LOGIN = os.environ['SERVICE_LOGIN']
SERVICE_PASSWORD = os.environ['SERVICE_PASSWORD']
