#!/usr/bin/env python3
"""lIFO Caching sytem module."""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A class representing a LIFO caching system."""

    def put(self, key, item):
        """
        Assign a value to a dict key.

        args:
            key: the dict key
            value: the value to be assigned to the key
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    discard_key, _ = self.cache_data.popitem()
                    print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Get a value corresponding to a key.

        args:
            key: the key
        Return:
            the value corresponding to the key

        """
        value = self.cache_data.get(key)
        return None if not key or not value else value
