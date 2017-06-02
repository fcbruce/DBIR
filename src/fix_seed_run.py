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

import cv2
import skimage.io as skio
import matplotlib.pyplot as plt

image_folder = '../data/256_ObjectCategories/'

def run(database, feature):

    nn = database.nearest_neighbor(feature)
    knns = database.knn(50, feature)
    return nn, knns

if __name__ == '__main__':
    
    keys, dataset, queries = load_features(db=15, seed=19941129)
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

    highest_q = None
    highest_ap = 0

    # for q in queries:
    #     # print q[1]

    #     nn, knns = run(database, q[2])
    #     # print keys[nn]
    #     ap50 = .0
    #     ap10 = .0
    #     j = 0.
    #     i = 0.
    #     n = len(knns)
    #     for knn in knns:
    #         # print keys[knn],
    #         j += 1
    #         if q[1][:3] == keys[knn][:3]: 
    #             i += 1
    #             ap50 += i / j / 50
    #             ap10 += i / j / 10
    #         if j == 10: map10 += ap10

    #     if ap10 > highest_ap: 
    #         highest_ap = ap10
    #         highest_q = q
    #     # print
    #     map50 += ap50

    #     if q[1][:3] == keys[nn][:3]: hit += 1

    # print 'top - 1: ', hit / len(queries)
    # print 'top - 10: ', map10 / len(queries)
    # print 'top - 50: ', map50 / len(queries)

    print highest_q, highest_ap
    highest_q = queries[-157]
    nn, knns = run(database, highest_q[2])
    cat_path = os.path.join(image_folder, highest_q[0])
    q_path = os.path.join(cat_path, highest_q[1])
    all_cat = os.listdir(image_folder)
    print q_path
    pathes = []
    for i in range(10):
        nn_path = os.path.join(image_folder, all_cat[int(keys[knns[i]][:3]) - 1], keys[knns[i]])
        print nn_path, keys[knns[i]]
        pathes.append(nn_path)

    q_im = skio.imread(q_path)
    q_im = cv2.resize(q_im, (224, 224))
    imgs = [skio.imread(path) for path in pathes]
    imgs = [ cv2.resize(img, (224, 224)) for img in imgs]
    # print imgs

    fig = plt.figure()
    plt.axis('off')
    plt.title('Query Image')
    plt.imshow(q_im)
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=5)
    plt.title('Inception V3')
    ax = axes.ravel()
    # print q_im
    # plt.imshow(q_im)
    # plt.show()

    for i in range(5): 
        ax[i] = plt.subplot(1, 5, i + 1)
        ax[i].axis('off')

    # plt.imshow(q_im)
    for i in range(0, 5):
        # plt.subplot(i)
        # plt.imshow(imgs[i - 1])
        ax[i].imshow(imgs[i])

    plt.show()


    
