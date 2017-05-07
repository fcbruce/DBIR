#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Sat 06 May 2017 17:10:14
#
#

import numpy as np
import falconn as fa

a = np.random.randn(50000, 500)
a /= np.linalg.norm(a, axis=1).reshape(-1, 1)

print "pending..."
params_cp = fa.LSHConstructionParameters()
params_cp.dimension = 500;
params_cp.lsh_family = 'cross_polytope'
params_cp.distance_function = 'euclidean_squared'
params_cp.l = 7
params_cp.num_rotations = 1
params_cp.seed = 11111
params_cp.num_setup_threads = 0
params_cp.storage_hash_table = 'bit_packed_flat_hash_table'
fa.compute_number_of_hash_functions(18, params_cp)

table = fa.LSHIndex(params_cp)
table.setup(a)

print "find"
print table.find_nearest_neighbor(a[1])
