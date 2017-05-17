#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Sun 14 May 2017 17:51:03
#
#

from keras.applications.xception import Xception, preprocess_input

from FeatureGenerator import FeatureGenerator

class XceptionFeatureGenerator(FeatureGenerator):

    def __init__(self, weights='imagenet'):
        FeatureGenerator.__init__(self, Xception, (299, 299), preprocess_input, weights, pooling='avg')
