from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse


def get_hostname(url: str):
    url = urlparse(url).hostname
    if not url:
        return
    found_dot = False
    for i, c in enumerate(reversed(url)):
        if c != '.':
            continue
        if not found_dot:
            found_dot = True
        else:
            return url[len(url)-i:]
    return url


def crawl_thread(executor, current_url, base_url, html_parser, visited_urls, futures):
    visited_urls.add(current_url)
    children = html_parser.getUrls(current_url)
    for child in children:
        if (child not in visited_urls) and (get_hostname(child) == base_url):
            future = executor.submit(crawl_thread, executor, child, base_url, html_parser, visited_urls, futures)
            futures.add(future)


class Solution:
    def crawl(self, start_url, html_parser):
        base_url = get_hostname(start_url)
        visited_urls = set([start_url])
        futures = set()

        with ThreadPoolExecutor(max_workers=500) as executor:
            initial_future = executor.submit(crawl_thread, executor, start_url,
                                             base_url, html_parser, visited_urls, futures)
            futures.add(initial_future)
            for future in as_completed(futures):
                # Spinlock until all threads complete
                pass

        return list(visited_urls)
