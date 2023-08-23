#!/usr/bin/env python3
"""LFU Caching sytem module."""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A class representing a least frequently used caching system."""

    def __init__(self):
        """Initialize a LRUCache instance."""
        super().__init__()
        self.LFU_dict = {}

    def put(self, key, item):
        """
        Assign a value to a dict key.

        args:
            key: the dict key
            value: the value to be assigned to the key
        """
        if key and item:
            if key in self.LFU_dict.keys():
                value = self.LFU_dict.pop(key)
                self.LFU_dict[key] = value + 1
            else:
                self.LFU_dict[key] = 1
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                sorted_list = sorted(self.LFU_dict.items(),
                                     key=lambda item: item[1])
                discard_key, _ = sorted_list[0]
                if discard_key == key:
                    discard_key, _ = sorted_list[1]
                del self.LFU_dict[discard_key]
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")

    def get(self, key):
        """
        Get a value corresponding to a key.

        args:
            key: the key
        Return:
            the value corresponding to the key

        """
        value = self.cache_data.get(key)
        if not key or not value:
            return None
        count = self.LFU_dict.pop(key)
        self.LFU_dict[key] = count + 1
        return value
