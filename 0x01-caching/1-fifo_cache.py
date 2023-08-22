#!/usr/bin/env python3
"""FIFO Caching sytem module."""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A class representing a FIFO caching system."""

    def put(self, key, item):
        """
        Assign a value to a dict key.

        args:
            key: the dict key
            value: the value to be assigned to the key
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                ordered_dict = OrderedDict(self.cache_data)
                discard_key = next(iter(ordered_dict))
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
        return None if not key or not value else value
