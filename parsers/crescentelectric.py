import repo
from collectors import basic
from headers import random_headers
from proxies import random_proxies


def extract_content(url, soup):
    return soup

def store_content(url, content):
    # store in a hash with the URL as the key and the title as the content
    repo.set_content(url, content)


def allow_url_filter(url):
    return True  # allow all by default


def get_html(url):
    return basic.get_html(url)

