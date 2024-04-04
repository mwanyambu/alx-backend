#!/usr/bin/env python3

""" MRUCache """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ inherits from caching system BaseCaching """

    def __init__(self):
        """ initializes MRUCache """
        super().__init__()
        self.odereddict = []

    def put(self, key, item):
        """ adds items to cache """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:  # nopep8
                print("DISCARD: {}".format(self.odereddict[-1]))
                del self.cache_data[self.odereddict[-1]]
                del self.odereddict[-1]
            if key in self.odereddict:
                del self.odereddict[self.odereddict.index(key)]
            self.odereddict.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ gets item by key """
        if key is not None and key in self.cache_data.keys():
            del self.odereddict[self.odereddict.index(key)]
            self.odereddict.append(key)
            return self.cache_data[key]
        return None
