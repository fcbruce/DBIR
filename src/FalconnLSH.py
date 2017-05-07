#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Sun 07 May 2017 16:03:13
#
#

import falconn as fa

class FalconnLSH:

    @staticmethod
    def get_params():
        return fa.LSHConstructionParameters()

    def __init__(self, dataset, params, num_bits=16):

        fa.compute_number_of_hash_functions(num_bits, params)
        self._table = fa.LSHIndex(params)
        self._table.setup(dataset)

    def nearest_neighbor(self, data):

        return self._table.find_nearest_neighbor(data)
    
    def knn(self, k, data):

        return self._table.find_k_nearest_neighbors(data, k)
