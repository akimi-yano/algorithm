# 535. Encode and Decode TinyURL
# Medium

# 788

# 1649

# Add to List

# Share
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


# This solution works:

class Codec:
    def __init__(self):
        self.short_long = {}
        self.count = 0
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.short_long[hash(longUrl)] = longUrl
        return hash(longUrl)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_long[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


# This solution works:

class Codec:
    def __init__(self):
        self.short_long = {}
        self.count = 0
        self.url_prefix = 'https://short.url/'
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.count += 1
        self.short_long[self.count] = longUrl
        return self.url_prefix + str(self.count)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_long[int(shortUrl.rsplit('/')[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))