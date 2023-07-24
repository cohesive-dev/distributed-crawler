import repo
from collectors import basic
from headers import random_headers
from proxies import random_proxies
import re

def extract_content(url, soup):
    text = soup.text
    text = re.sub(r'\n+', '\n', text).strip()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def store_content(url, content):
    # store in a hash with the URL as the key and the title as the content
    repo.set_content(url, content)


def allow_url_filter(url):
    return True  # allow all by default


def get_html(url):
    return basic.get_html(url)

