from lib.library import *
from lib.db_connection import *



def main():
    banner()
    url, port = menu()
    test = get_page_extension(url)
    print(test)


    


if __name__ =="__main__":
    main()