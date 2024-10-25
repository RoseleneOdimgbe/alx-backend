#!/usr/bin/env python3

"""This implements a LIFO caching system"""

from typing import Any, Union

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements a LIFO caching system"""

    def __init__(self) -> None:
        """Initializes the instance"""
        super().__init__()
        self.keys = []

    def put(self, key: Any, item: Any) -> None:
        """Inserts an item into the cache"""
        if any(obj is None for obj in (key, item)):
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = self.keys.pop()
            del self.cache_data[last]
            print(f"DISCARD: {last}")

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key: Any) -> Union[Any, None]:
        """Returns the item with the given key if it exists, else None"""
        return self.cache_data.get(key, None)
