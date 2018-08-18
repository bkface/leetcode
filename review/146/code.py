# https://leetcode.com/problems/lru-cache/description/

from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self._cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._cache:
            return -1

        value = self._cache[key]
        self._cache.pop(key)
        self._cache[key] = value
        return value

    def has_capacity(self):
        return len(self._cache) < self.capacity

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self._cache:
            self._cache.pop(key)
        elif not self.has_capacity():
            lru = self._cache.keys()[0] # exception raised if capacity=0
            self._cache.pop(lru)
        self._cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
