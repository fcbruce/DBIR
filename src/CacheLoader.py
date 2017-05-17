#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 02 May 2017 19:46:15
#
#

import redis

from decorators import singleton

class CacheLoader:

    def __init__(self, host='localhost', port=6379, db=0, flush_db=False):
        pool = redis.ConnectionPool(host=host, port=port, db=db)
        self.redis = redis.Redis(connection_pool=pool)
        if flush_db:
            self.redis.flushdb()

    def get(self, key):
        return self.redis.get(key)

    def set(self, key, value):
        self.redis.set(key, value)

    def exists(self, key):
        return self.redis.exists(key)

    def get_all_keys(self):
        return self.redis.keys()
