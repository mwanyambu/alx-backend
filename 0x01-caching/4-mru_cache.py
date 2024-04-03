#!/usr/bin/python3

"""MRUCache """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ inherits from caching system BaseCaching """

    def __init__(self):
        """ initializes MRUCache """
        super().__init__()
        self.odereddict = []

    def put(self, key, item):
        """ adds items to cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recent = self.odereddict.pop()
                self.cache_data.pop(most_recent)
                print("DISCARD:", most_recent)
            self.cache_data[key] = item
            self.odereddict.append(key)

    def get(self, key):
        """ gets item by key """
        if key is not None and key in self.cache_data:
            self.odereddict.remove(key)
            self.odereddict.append(key)
            return self.cache_data.get(key)
