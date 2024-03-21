import os
from dotenv import load_dotenv
load_dotenv()

APP_ENV = os.getenv('APP_ENV')

#smptlib credentials
EMAIL_ADDRESS_SMPT = os.getenv('EMAIL_ADDRESS_SMPT')
PASSWORD_SMPT = os.getenv('PASSWORD_SMPT')

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')