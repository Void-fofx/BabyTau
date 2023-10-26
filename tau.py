from lib.library import Tau, banner, menu
from lib.db_connection import connect, read_sql, execute_sql, execute_sql_no_return


def main():
    banner()
    url, port = menu()
    t = Tau(url, port)
    t.set_ips()
    t.scrape_js()
    t.scrape_urls()

    


if __name__ =="__main__":
    main()