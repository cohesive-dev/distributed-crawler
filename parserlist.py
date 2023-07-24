from urllib.parse import urlparse
from parsers import defaults, crescentelectric


parsers = {
    'www.crescentelectric.com': crescentelectric
}


def get_parser(url):
    hostname = urlparse(url).hostname  # extract domain from URL
    if hostname in parsers:
        # use the dict above to return the custom parser if present
        return parsers[hostname]

    return defaults
