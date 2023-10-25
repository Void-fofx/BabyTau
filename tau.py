from functions import Tau, banner, menu


def main():
    banner()
    url, port = menu()
    t = Tau(url, port)
    t.connect()
    t.set_ips()
    


if __name__ =="__main__":
    main()