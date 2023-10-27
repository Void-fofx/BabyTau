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


def http_get(url: str) -> str:
    print("Sending HTTP GET...")
    resp = req.get(url)
    print(f"Server returned {resp}")
    return resp.text

def get_path(url: str) -> str:
    return urlparse(url).path

def get_protocol(url: str) -> str:
    return urlparse(url).scheme

def get_params(url: str) -> [str]:
    return urlparse(url).params

def get_page_extension(url: str) -> str:
    path = urlparse(url).path
    split = os.path.split(path)
    dot_index = split[-1].find('.')
    return split[-1][dot_index:]

def get_tl_domain(url: str):
    pass

def get_subdomains(url: str):
    pass

def http_post(url: str) -> str:
    print("Sending HTTP POST...")
    resp = req.post(url)
    print(f"Server returned {resp}")
    return resp.text

def get_ipv4(url: str):
    print("Acquiring ip address")
    v4 = socket.getaddrinfo(url, None, socket.AF_INET)
    (_, _, _, _, (ipv4,_)) = v4[0]
    return ipv4

def get_ipv6(url: str):
    v6 = socket.getaddrinfo(url, None, socket.AF_INET6)
    (_, _, _, _, (ipv6,_,_,_)) = v6[0]
    return ipv6

def scrape_js(html: str):
    soup = bs(html, 'html.parser')
    return soup.find_all('script')

def scrape_urls(html: str):
    soup = bs(html, 'html.parser')
    return soup.find_all('a')


def show_html_pretty(html: str):
    soup = bs(html, 'html.parser')
    print(soup.prettify())
    return soup.prettify()

def set_site_info(url: str, port: int) -> {}:
    db_site = {}
    html = http_get(url)
    db_site['full_url'] = url
    db_site['port'] = port
    db_site['html'] = html
    db_site['endpoint_path'] = get_path(url)
    db_site['protocol'] = get_protocol(url)
    db_site['params'] = get_params(url)
    db_site['page_extension'] = get_page_extension(url)
    db_site['tl_domain'] = get_tl_domain(url)
    db_site['sub_domains'] = get_subdomains(url)
    return db_site

def set_page_info(url: str, port: int) -> {}:
    db_page = {}
    db_page['comments'] = None
    db_page['js_code'] = None
    db_page['js_urls'] = None
    db_page['page_extension'] = None
    db_page['params'] = None
    db_page['urls'] = None
    db_page['post_resp'] = None
    db_page['get_resp'] = None
    db_page['options_resp'] = None
    db_page['put_resp'] = None
    db_page['patch_resp'] = None
    db_page['head_resp'] = None
    return db_page

def set_page_data_info(url: str, port: int) -> {}:
    db_page_data = {}
    db_page_data['full_url'] = None
    db_page_data['endpoint_path'] = None
    db_page_data['protocol'] = None
    db_page_data['params'] = None
    db_page_data['page_extension'] = None
    db_page_data['port'] = None
    db_page_data['tl_domain'] = None
    db_page_data['sub_domains'] = None
    db_page_data['options_resp'] = None
    db_page_data['put_resp'] = None
    db_page_data['patch_resp'] = None
    db_page_data['head_resp'] = None
    return db_page_data











: '',
	: '',
	: '',
	: [],
	: '',
	: '',
	: '',
	: []