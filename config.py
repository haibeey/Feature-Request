import os
import datetime


DB_PATH = os.path.join(os.path.dirname(__file__), 'temp.db')
SECRET_KEY = 'jkhdlgblsjdkhgu4weg7uerhu39oh[erorujdsoik' 
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DB_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER=os.getcwd()+'\\uploads'
DEBUG = True
