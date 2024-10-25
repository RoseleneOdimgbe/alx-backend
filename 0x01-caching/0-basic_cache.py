#!/usr/bin/env python3

"""This implements a basic caching module"""

from typing import Any, Union

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implements a basic caching system"""

    def put(self, key: Any, item: Any) -> None:
        """Inserts an item into the cache."""
        if any(obj is None for obj in (key, item)):
            return

        self.cache_data[key] = item

    def get(self, key) -> Union[Any, None]:
        """Returns the item with the given key if it exists, else None"""
        return self.cache_data.get(key, None)
