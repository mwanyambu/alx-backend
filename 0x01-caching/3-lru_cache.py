#!/usr/bin/env python3

""" lru cache """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ inherits from caching system BaseCaching """

    def __init__(self):
        """ initialize LRUCache """
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        """ add items """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_queue.remove(key)
            self.key_queue.append(key)
            if len(self.cache_data) >= self.MAX_ITEMS:
                learst_recent = self.key_queue.pop(0)
                print("DISCARD:", learst_recent)
                del self.cache_data[learst_recent]
            self.cache_data[key] = item

    def get(self, key):
        """ gets items by key """
        if key is not None:
            if key in self.cache_data:
                self.key_queue.remove(key)
                self.key_queue.append(key)
                return self.cache_data.get(key)
        return None
