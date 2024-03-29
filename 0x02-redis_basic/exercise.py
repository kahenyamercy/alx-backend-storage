#!/usr/bin/env python3

"""
This module provides a Cache class for interacting with Redis.
"""

import redis
import uuid
from typing import Union

class Cache:
    """
    A class for caching data using Redis.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache class with a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store input data in Redis and return a randomly generated key.

        Args:
            data: The data to be stored in the cache. It can be a string,
                  bytes, integer, or float.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
