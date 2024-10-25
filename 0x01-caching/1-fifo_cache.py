#!/usr/bin/env python3

"""This implements a FIFO caching system"""

from typing import Any, Union

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implements a FIFO caching system"""

    def __init__(self) -> None:
        """Initializes the instance"""
        super().__init__()
        self.keys = []

    def put(self, key: Any, item: Any) -> None:
        """Inserts an item into the cache"""
        if any(obj is None for obj in (key, item)):
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first = self.keys.pop(0)
            del self.cache_data[first]
            print(f"DISCARD: {first}")

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key: Any) -> Union[Any, None]:
        """Returns the item with the given key if it exists, else None"""
        return self.cache_data.get(key, None)
