# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:45:42 2019

@author: Nagasudhir

access environment variables in python - https://stackoverflow.com/questions/4906977/how-to-access-environment-variable-values
"""

from sqlalchemy import create_engine
# from sqlalchemy.orm import relationship
# from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import os


def getDbConfig():
    db_config = {'drivername': 'postgres',
                 'username': 'postgres',
                 'password': 'pass',
                 'host': 'hostip',
                 'database': 'mis_warehouse_db',
                 'port': 5432}
    # print(os.environ['PATH'])
    # get the username from environment variable if present
    db_config['database'] = os.getenv('MIS_WAREHOUSE_DB_NAME', 'db_name')

    # get the username from environment variable if present
    db_config['username'] = os.getenv('MIS_WAREHOUSE_DB_USERNAME', 'username')

    # get the password from environment variable if present
    db_config['password'] = os.getenv('MIS_WAREHOUSE_DB_PASSWORD', 'password')

    # get the host ip from environment variable if present
    db_config['host'] = os.getenv('MIS_WAREHOUSE_DB_HOST', 'hostip')

    return db_config


Base = declarative_base()


class MISDBHelper:
    db_uri = None
    engine = None

    def __init__(self, db_config_dict):
        self.db_uri = URL(**db_config_dict)
        self.engine = create_engine(self.db_uri)

    def create_db(self):
        # create all tables if db does not exists
        Base.metadata.create_all(self.engine)

    def get_engine(self):
        return self.engine
