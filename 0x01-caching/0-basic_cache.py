#!/usr/bin/env python3
"""Caching sytem module."""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A class representing a caching system."""

    def put(self, key, item):
        """
        Assign a value to a dict key.

        args:
            key: the dict key
            value: the value to be assigned to the key
        """
        if key and item:
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
