#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Sun 07 May 2017 15:34:08
#
#

import numpy as np

def normalize(array):
    
    if not isinstance(array, np.ndarray):
        raise ValueError("normalize need a numpy array")

    return array / np.linalg.norm(array, axis=1).reshape(-1, 1)
