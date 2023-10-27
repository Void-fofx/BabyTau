import psycopg2 as pg
from dotenv import load_dotenv
import os
load_dotenv()


CREDS = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME')
}

def db_connect():
    try:
        conn = pg.connect(**CREDS)
    except pg.OperationalError as e:
        print("Unable to connect to the database", e)
    return conn

def read_sql(filename: str):
    with open(f"sql/{filename}.sql", 'r') as f:
        sql = f.read()
    return sql

def execute_sql_no_return(sql: str, conn: pg.connect, params = None):
    if params is None:
        params = {}

    with conn.cursor() as cur:
        cur.execute(sql, params)
        conn.commit()
        cur.close()

def execute_sql(sql: str, conn: pg.connect, params = None):
    if params is None:
        params = {}
        
    with conn.cursor() as cur:
        cur.execute(sql, params)
        result = cur.fetchall()
        return result