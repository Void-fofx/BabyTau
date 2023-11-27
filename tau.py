from lib.library import banner, menu, set_site_info, set_page_info
from lib.db_connection import db_connect, init_db_tables, save_site, save_page



def main():
    conn = db_connect()
    init_db_tables(conn)
    banner()
    url, port = menu()
    site = set_site_info(url, port)
    save_site(conn, site)
    page = set_page_info(url, port)
    save_page(conn, page)


if __name__ =="__main__":
    main()
