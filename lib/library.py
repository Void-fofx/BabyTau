from lib.banner import banner
import tldextract as tld
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

def get_netloc(url: str) -> str:
    return urlparse(url).netloc

def get_path(url: str) -> str:
    return urlparse(url).path

def get_protocol(url: str) -> str:
    return urlparse(url).scheme

def get_params(url: str) -> [str]:
    params = urlparse(url).params
    return [x for x in params]

def get_page_extension(url: str) -> str:
    path = urlparse(url).path
    split = path.rsplit('.', 1)
    return split[-1]
    

def get_tl_domain(url: str) -> str:
    result = tld.extract(url)
    return result.fqdn

def get_sub_domains(url: str) -> [str]:
    subs = tld.extract(url)
    split = subs.subdomain.rsplit('.')
    return split

def http_post(url: str) -> str:
    print("Sending HTTP POST...")
    resp = req.post(url)
    print(f"Server returned {resp.status_code}")
    return resp.text

def get_ipv4(url: str) -> str:
    try:
        v4 = socket.gethostbyname(url)
    except OSError as e:
        v4 = None
        print("Unable to find IPv4 address.")
    return v4

def get_ipv6(url: str) -> str:
    try:
        v6 = socket.getaddrinfo(url, None, socket.AF_INET6)[0][4][0]
    except OSError as e:
        v6 = None
        print("Unable to find IPv6 address.")
    return v6

def scrape_js(html: str) -> [str]:
    soup = bs(html, 'html.parser')
    return soup.find_all('script')

def scrape_urls(html: str) -> [str]:
    soup = bs(html, 'html.parser')
    return soup.find_all('a')


def get_html_pretty(html: str) -> str:
    soup = bs(html, 'html.parser')
    return soup.prettify()

def set_site_info(url: str, port: int) -> object:
    db_site = {}
    db_site['full_url'] = url
    db_site['endpoint_path'] = get_path(url)
    db_site['protocol'] = get_protocol(url)
    db_site['params'] = get_params(url)
    db_site['page_extension'] = get_page_extension(url)
    db_site['port'] = port
    db_site['tl_domain'] = get_tl_domain(url)
    db_site['sub_domains'] = get_sub_domains(url)
    db_site['ipv4'] = get_ipv4(get_netloc(url))
    db_site['ipv6'] = get_ipv6(get_netloc(url))
    return db_site

def set_page_info(url: str, port: int) -> object:
    db_page = {}
    db_page['full_url'] = url
    db_page['endpoint_path'] = get_path(url)
    db_page['protocol'] = get_protocol(url)
    db_page['params'] = get_params(url)
    db_page['page_extension'] = get_page_extension(url)
    db_page['port'] = port
    db_page['tl_domain'] = get_tl_domain(url)
    db_page['sub_domains'] = get_sub_domains(url)
    db_page['homepage'] = False
    return db_page

def set_page_data_info(url: str, port: int) -> object:
    db_page_data = {}
    db_page_data['html'] = None
    db_page_data['html_pretty'] = None
    db_page_data['comments'] = None
    db_page_data['js_code'] = None
    db_page_data['js_urls'] = None
    db_page_data['page_extension'] = None
    db_page_data['params'] = None
    db_page_data['urls'] = None
    db_page_data['post_resp'] = None
    db_page_data['get_resp'] = None
    db_page_data['options_resp'] = None
    db_page_data['put_resp'] = None
    db_page_data['patch_resp'] = None
    db_page_data['head_resp'] = None
    return db_page_data
