#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 15 May 2017 22:48:20
#
#

from keras.applications.resnet50 import ResNet50, preprocess_input

from FeatureGenerator import FeatureGenerator

class Res50FeatureGenerator(FeatureGenerator):

    def __init__(self, weights='imagenet'):
        FeatureGenerator.__init__(self, ResNet50, (224, 224), preprocess_input, weights, pooling='avg')

