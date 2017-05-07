#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 02 May 2017 20:08:45
#
#

def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance
