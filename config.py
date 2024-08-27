# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/foodie-II'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get  ('8203706864c60447df136538d6378d79e6cdfb736c798e3efe4c935d2a168545')
