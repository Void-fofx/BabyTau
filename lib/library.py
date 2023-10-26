from lib.banner import banner
import requests as req
import socket
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
_OS = os.name


def menu() -> []:
    url = str(input("[+] Please enter the target url: "))
    port = int(input("[+] Please enter the target port: "))
    return [url, port]

# TODO add functionality to guess technologies used on page
class Tau():
    def __init__(self, url: str = 'localhost', port: int = 80):
        self.url = url
        self.host = urlparse(url).netloc
        self.port = port
        self.ip4 = 'not set'
        self.ip6 = 'not set'
        self.path = urlparse(url).path
        self.html = 'not set'
        self.urls = [str]
        self.js_urls = [str]
        self.js = [str]
        self.comments = [str]

        self.http_get()
    

    def http_get(self):
        print("Sending HTTP GET...")
        resp = req.get(self.url)
        print(f"Server returned {resp}")
        self.html = resp.text

    def set_ips(self):
        print("Acquiring ip address")
        v6 = socket.getaddrinfo(self.host, None, socket.AF_INET6)
        (_, _, _, _, (ipv6,_,_,_)) = v6[0]
        self.ip6 = ipv6
        v4 = socket.getaddrinfo(self.host, None, socket.AF_INET)
        (_, _, _, _, (ipv4,_)) = v4[0]
        self.ip4 = ipv4


    def scrape_js(self):
        soup = bs(self.html, 'html.parser')
        print(soup.find_all('script'))

    def scrape_urls(self):
        soup = bs(self.html, 'html.parser')
        print(soup.find_all('a'))


    def show_html_pretty(self):
        soup = bs(self.html, 'html.parser')
        print(soup.prettify())

