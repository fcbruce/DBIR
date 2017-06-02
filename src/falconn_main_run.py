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

image_folder = '../data/256_ObjectCategories/'

def run(database, feature):

    nn = database.nearest_neighbor(feature)
    knns = database.knn(50, feature)
    return nn, knns

if __name__ == '__main__':
    
    keys, dataset, queries = load_features(db=13)
    dataset = normalize(dataset)

    params = FalconnLSH.get_params()
    params.dimension = dataset.shape[1]
    params.lsh_family = 'cross_polytope'
    params.distance_function = 'negative_inner_product'
    params.k = 17
    params.l = 31
    params.storage_hash_table = 'flat_hash_table'
    params.num_rotations = 1
    params.num_setup_threads = 0

    database = FalconnLSH(dataset, params)

    hit = 0.
    map10 = 0.0
    map50 = 0.0

    for q in queries:
        # print q[1]

        nn, knns = run(database, q[2])
        # print keys[nn]
        ap50 = .0
        ap10 = .0
        j = 0.
        i = 0.
        n = len(knns)
        for knn in knns:
            # print keys[knn],
            j += 1
            if q[1][:3] == keys[knn][:3]: 
                i += 1
                ap50 += i / j / 50
                ap10 += i / j / 10
            if j == 10: map10 += ap10
        # print
        map50 += ap50

        if q[1][:3] == keys[nn][:3]: hit += 1

    print 'top - 1: ', hit / len(queries)
    print 'top - 10: ', map10 / len(queries)
    print 'top - 50: ', map50 / len(queries)


    
