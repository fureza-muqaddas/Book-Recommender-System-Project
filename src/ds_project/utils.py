import os 
import sys
from src.ds_project.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql
import yaml
from yaml import safe_load
from src.ds_project.exception import AppException
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
db = os.getenv("db")
password = os.getenv("password")

def read_sql_data():
    logging.info("Reading data from SQL database.")
    try:
        mybd = pymysql.connect(host=host, user=user, password=password, db=db)
        logging.info("Data read from SQL database successfully.")
        df=pd.read_sql("SELECT * FROM books", con=mybd)
        return df
        
    except Exception as e:
        raise AppException(e, sys) from e



def read_yaml_file(file_path:str) ->dict:
    '''
    Reads a YAML file and returns the contents as a dictionary file_pat: str
    '''

    try:
        with open(file_path, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e
    
    






