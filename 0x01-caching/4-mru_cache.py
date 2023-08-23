#!/usr/bin/env python3
"""MRU Caching sytem module."""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A class representing a most recently used caching system."""

    def __init__(self):
        """Initialize a LRUCache instance."""
        super().__init__()
        self.MRU_list = []

    def put(self, key, item):
        """
        Assign a value to a dict key.

        args:
            key: the dict key
            value: the value to be assigned to the key
        """
        if key and item:
            if key in self.MRU_list:
                self.MRU_list.remove(key)
            self.MRU_list.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            discard_idx = len(self.MRU_list) - 2
            discard_key = self.MRU_list.pop(discard_idx)
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
        if key in self.MRU_list:
            self.MRU_list.remove(key)
        self.MRU_list.append(key)
        return value
