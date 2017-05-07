#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Sun 07 May 2017 15:06:37
#
#

import numpy as np
import json

from CacheLoader import CacheLoader

def load_features():

    cache = CacheLoader()
    keys = cache.get_all_keys()
    dataset = np.array([json.loads(cache.get(key)) for key in keys], dtype=np.float32)

    return keys, dataset
    

if __name__ == '__main__':
    load_feature()
