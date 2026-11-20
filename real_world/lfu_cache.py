"""
LFU (Least Frequently Used) Cache
Evicts the least frequently used item. Ties broken by LRU order.

Time:  O(1) for get and put
Space: O(capacity)
"""
from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._increment_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._increment_freq(key)
            return

        if len(self.key_to_val) >= self.capacity:
            self._evict()

        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    def _increment_freq(self, key: int):
        freq = self.key_to_freq[key]
        self.key_to_freq[key] = freq + 1
        del self.freq_to_keys[freq][key]

        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.freq_to_keys[freq + 1][key] = None

    def _evict(self):
        keys = self.freq_to_keys[self.min_freq]
        evict_key, _ = keys.popitem(last=False)
        if not keys:
            del self.freq_to_keys[self.min_freq]
        del self.key_to_val[evict_key]
        del self.key_to_freq[evict_key]


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))    # 1 (freq of 1 becomes 2)
    cache.put(3, 3)        # evicts key 2 (freq 1, LRU)
    print(cache.get(2))    # -1
    print(cache.get(3))    # 3
    cache.put(4, 4)        # evicts key 3 (freq 1)
    print(cache.get(1))    # 1
    print(cache.get(3))    # -1
    print(cache.get(4))    # 4
