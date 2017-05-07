#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Sun 07 May 2017 16:21:49
#
#

from FalconnLSH import *
from load_features import *
from utils import *

def run(i, key, dataset, database):

    q = database.nearest_neighbor(dataset[i])
    knns = database.knn(5, dataset[i])
    print key[i], key[q]
    for nn in knns:
        print keys[nn],
    print 


if __name__ == '__main__':
    
    keys, dataset = load_features()
    dataset = normalize(dataset)

    params = FalconnLSH.get_params()
    params.dimension = dataset.shape[1]
    params.lsh_family = 'cross_polytope'
    params.distance_function = 'euclidean_squared'
    params.k = 7
    params.l = 11
    params.storage_hash_table = 'bit_packed_flat_hash_table'
    params.num_rotations = 1
    params.num_setup_threads = 0

    database = FalconnLSH(dataset, params)

    run(0, keys, dataset, database)

    run(7, keys, dataset, database)

    run(1024, keys, dataset, database)

    
