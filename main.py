from tasks import queue_url
import repo
import logging

starting_url = 'https://www.crescentelectric.com/'
repo.add_to_visit(starting_url)
maximum_items = 10
logger = logging.getLogger(__name__)

while True:
    queued = repo.count_queued()
    visited = repo.count_visited()
    total = queued
    print('Visited', visited)
    if total >= maximum_items:
        print('Exiting! Over maximum:', total)
        break

    # timeout after 1 minute
    item = repo.pop_to_visit_blocking(60)
    if item is None:
        print('Timeout! No more items to process')
        break

    url = item[1].decode('utf-8')
    print('Pop URL', url)
    queue_url.delay(url, maximum_items)
