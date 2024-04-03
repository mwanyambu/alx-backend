#!/usr/bin/env python3

""" LUFCache """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ inherits from a chaching system BaseCaching """

    def __init__(self):
        """initialize LFUCache """
        super().__init__()
        self.learst_frequent = {}

    def put(self, key, item):
        """ add items to cache """
        if not(key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                lused = min(self.learst_frequent, key=self.learst_frequent.get)
                self.learst_frequent.pop(lused)
                self.cache_data.pop(lused)
                print("DISCARD: {}".format(lused))
            if not (key in self.learst_frequent):
                self.learst_frequent[key] = 0
            else:
                self.learst_frequent[key] += 1

    def get(self, key):
        """ get items by key """
        if key is None or key not in self.cache_data:
            return None
        self.learst_frequent[key] += 1
        return self.cache_data.get(key)
