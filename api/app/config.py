import os

from dotenv import load_dotenv


load_dotenv()


APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")