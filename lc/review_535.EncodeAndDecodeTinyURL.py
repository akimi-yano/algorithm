# 535. Encode and Decode TinyURL
# Medium

# 854

# 1741

# Add to List

# Share
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and 
# it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode 
# algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be 
# decoded to the original URL.


# This solution works:


class Codec:
    def __init__(self):
        self.storage = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = hash(longUrl)
        self.storage[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.storage[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))