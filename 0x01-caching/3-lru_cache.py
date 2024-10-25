#!/usr/bin/env python3

"""This implements the LRU caching algorithm"""

from typing import (
    Any,
    Union,
)

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implements an LRU caching algorithm"""

    def __init__(self):
        """Initializes the instance"""
        super().__init__()
        self.keys = []

    def put(self, key: Any, item: Any) -> None:
        """Insert an item into the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = self.keys.pop(0)
            del self.cache_data[last]
            print(f"DISCARD: {last}")

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key: Any) -> Union[Any, None]:
        """Return the item with the given key if it exists, else None"""
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
