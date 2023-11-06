from lib.library import *
from lib.db_connection import *



def main():
    conn = db_connect()
    init_db_tables(conn)
    banner()
    url, port = menu()
    site = set_site_info(url, port)
    save_site(conn, site)
    

# TODO use sql to insert some new data into db


if __name__ =="__main__":
    main()