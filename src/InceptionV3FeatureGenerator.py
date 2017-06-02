#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 17 May 2017 22:14:31
#
#

from keras.applications.inception_v3 import InceptionV3, preprocess_input

from FeatureGenerator import FeatureGenerator

class InceptionV3FeatureGenerator(FeatureGenerator):

    def __init__(self, weights='imagenet'):
        FeatureGenerator.__init__(self, InceptionV3, (299, 299), preprocess_input, weights, pooling='avg')
