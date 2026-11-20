"""
URL Shortener
Design a simple URL shortening service.

Features: Shorten, expand, custom aliases, click tracking.
"""
import hashlib
import string
import random
from datetime import datetime


class URLShortener:
    BASE62 = string.ascii_letters + string.digits

    def __init__(self, domain: str = "short.url"):
        self.domain = domain
        self.url_map = {}       # short_code -> long_url
        self.reverse_map = {}   # long_url -> short_code
        self.click_counts = {}  # short_code -> count
        self.created_at = {}    # short_code -> timestamp
        self.counter = 0

    def shorten(self, long_url: str, custom_alias: str = None) -> str:
        if long_url in self.reverse_map:
            return f"https://{self.domain}/{self.reverse_map[long_url]}"

        if custom_alias:
            if custom_alias in self.url_map:
                raise ValueError(f"Alias '{custom_alias}' already taken")
            short_code = custom_alias
        else:
            short_code = self._generate_code(long_url)

        self.url_map[short_code] = long_url
        self.reverse_map[long_url] = short_code
        self.click_counts[short_code] = 0
        self.created_at[short_code] = datetime.now()

        return f"https://{self.domain}/{short_code}"

    def expand(self, short_url: str) -> str:
        short_code = short_url.split("/")[-1]
        if short_code not in self.url_map:
            raise KeyError(f"Short URL not found: {short_url}")

        self.click_counts[short_code] += 1
        return self.url_map[short_code]

    def get_stats(self, short_code: str) -> dict:
        if short_code not in self.url_map:
            raise KeyError(f"Code not found: {short_code}")
        return {
            "short_code": short_code,
            "long_url": self.url_map[short_code],
            "clicks": self.click_counts[short_code],
            "created_at": self.created_at[short_code].isoformat(),
        }

    def _generate_code(self, url: str, length: int = 7) -> str:
        self.counter += 1
        hash_input = f"{url}{self.counter}{random.random()}"
        hash_val = hashlib.md5(hash_input.encode()).hexdigest()
        code = ""
        num = int(hash_val[:12], 16)
        while num > 0 and len(code) < length:
            code += self.BASE62[num % 62]
            num //= 62
        return code


if __name__ == "__main__":
    shortener = URLShortener()
    short = shortener.shorten("https://www.example.com/very/long/path/to/resource")
    print(f"Shortened: {short}")

    original = shortener.expand(short)
    print(f"Expanded: {original}")

    custom = shortener.shorten("https://github.com/myproject", custom_alias="myproject")
    print(f"Custom: {custom}")
