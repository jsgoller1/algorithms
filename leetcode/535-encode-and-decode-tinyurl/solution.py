"""
Statement

TinyURL is a URL shortening service where you enter a URL
such as https://leetcode.com/problems/design-tinyurl and
it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm
should work. You just need to ensure that a URL can be
encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

Input: a target url (encode), or an encoded url (decode)
Output: an encoded url (encode), or a target url (decode)
-----------------------
Understand / Plan

encoding:
- we need a collisionless way to encode a url to a tinyurl string
  - the actual encoding is just the URL path; we need to append or trim the "tinyurl" part.
  - the encoding should be a hash function of some kind, ideally not too long.
- decoding can be the path mapped to the target url in a dictionary

encode:
  - take md5 of string
  - use as path for url
  - install in dictionary
  - return to user

decode:
  - get path
  - lookup in dict
  - return target to user
"""

import hashlib


class Codec:
    def __init__(self):
        self.urlmap = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        md5 = hashlib.md5()
        md5.update(longUrl.encode())
        slug = md5.hexdigest()
        self.urlmap[slug] = longUrl
        return "http://tinyurl.com/" + slug

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        if shortUrl[:19] != "http://tinyurl.com/":
            return ""

        slug = shortUrl[19:]
        try:
            return self.urlmap[slug]
        except KeyError:
            return ""


if __name__ == '__main__':
    codec = Codec()
    urls = [
        "www.google.com",
        "http://jsgoller.github.io"
        "foo.bar.baz"
    ]
    for url in urls:
        assert url == codec.decode(codec.encode(url))
