#!/usr/bin/env python3
"""LRU Caching sytem module."""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A class representing a least resently used caching system."""

    def __init__(self):
        """Initialize a LRUCache instance."""
        super().__init__()
        self.LRU_list = []

    def put(self, key, item):
        """
        Assign a value to a dict key.

        args:
            key: the dict key
            value: the value to be assigned to the key
        """
        if key and item:
            if key in self.LRU_list:
                self.LRU_list.remove(key)
            self.LRU_list.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            discard_key = self.LRU_list[0]
            self.LRU_list.remove(discard_key)
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
        if key in self.LRU_list:
            self.LRU_list.remove(key)
        self.LRU_list.append(key)
        return value
