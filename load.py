import requests
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from config import postgresPass
from queries import gp_practice_query
from queries import air_pollution_query
from queries import national_gp_query
from queries import national_air_pollution_query

GP_PRACTICE_DF=pd.read_csv("gp_practice.csv")
GP_TIME_DATA_DF=pd.read_csv("air_pollution_data.csv")
NATIONAL_GP=pd.read_csv("national_gp.csv")
NATIONAL_AIR_POLLUTION=pd.read_csv("national_air_pollution.csv")

usr = 'postgres'
pwd = postgresPass
port = '5432'
db_name = 'birmingham_air_pollution'

engine = create_engine(f'postgresql://{usr}:{pwd}@localhost:{port}/{db_name}')

if not database_exists(engine.url):
    print("Creating database...")
    create_database(engine.url)

print("Database exists?", database_exists(engine.url))

engine.execute(gp_practice_query)
engine.execute(air_pollution_query)
engine.execute(national_gp_query)
engine.execute(national_air_pollution_query)

try:
    GP_PRACTICE_DF.to_sql(name = 'gp_practice', con = engine, if_exists='replace')
    GP_TIME_DATA_DF.to_sql(name = 'air_pollution_data', con = engine, if_exists='replace')
    NATIONAL_GP.to_sql(name = 'national_gp', con = engine, if_exists='replace')
    NATIONAL_AIR_POLLUTION.to_sql(name = 'national_air_pollution', con = engine, if_exists='replace')
    
except Exception as e:
    print(e)
