#!/usr/bin/env python3
""" class BasicCache """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching that is a caching system
    """

    def put(self, key, item):
        """ adds items to cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ gets items by key """
        if key is not None:
            return self.cache_data.get(key)
        return None
