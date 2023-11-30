# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

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


class Solution:
    def crawl(self, start_url: str, html_parser: 'HtmlParser') -> List[str]:
        hostname = get_hostname(start_url)
        visited = set()
        stack = [start_url]
        while stack:
            curr_url = stack.pop()
            if get_hostname(curr_url) != hostname:
                continue
            visited.add(curr_url)
            for child in html_parser.getUrls(curr_url):
                if child not in visited:
                    stack.append(child)
        return list(visited)
