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

def db_connect() -> pg.extensions.connection:
    try:
        conn = pg.connect(**CREDS)
    except pg.OperationalError as e:
        print("Unable to connect to the database", e)
    return conn

def read_sql(filename: str) -> str:
    with open(f"sql/{filename}.sql", 'r') as f:
        sql = f.read()
    return sql


def execute_sql(sql: str, conn: pg.extensions.connection, params = None):
    if params is None:
        params = {}
        
    with conn.cursor() as cur:
        cur.execute(sql, params)
        result = cur.fetchall()
        conn.commit()
        return result
    
def execute_sql_no_return(conn: pg.extensions.connection, sql: str, params = None):
    if params is None:
        params = {}

    with conn.cursor() as cur:
        cur.execute(sql, params)
        conn.commit()
    
def init_db_tables(conn: pg.extensions.connection) -> None:
    init_db = read_sql('init_db')
    execute_sql_no_return(conn, init_db)

def save_site(conn: pg.extensions.connection, params = None) -> None:
    site = read_sql('new_site')
    execute_sql_no_return(conn, site, params)

def save_page(conn: pg.extensions.connection, params = None) -> None:
    page = read_sql('new_page')
    execute_sql_no_return(conn, page, params)

