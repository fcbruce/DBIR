#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Sun 07 May 2017 15:06:37
#
#

import numpy as np
import json
import random
import os

from CacheLoader import CacheLoader

image_folder = '../data/256_ObjectCategories/'

def load_features(db=0):

    cache = CacheLoader(db=db)

    queries = []
    query_keys = set()
    
    for subfolder in os.listdir(image_folder):
        images = os.listdir(os.path.join(image_folder, subfolder))
        images = [ img for img in images if img.endswith('.jpg') ]
        keys = random.sample(images, 5)
        for key in keys:
            queries.append((subfolder, key, np.array(json.loads(cache.get(key)), dtype=np.float32)))
            query_keys.add(key)


    all_keys = cache.get_all_keys() 
    all_keys = [ key for key in all_keys if key not in query_keys]
    dataset = np.array([ json.loads(cache.get(key)) for key in all_keys ], dtype=np.float32)
    length = len(all_keys)
    key2id = dict(zip(all_keys, range(length)))

    return all_keys, dataset, queries
    

if __name__ == '__main__':
    load_features()
