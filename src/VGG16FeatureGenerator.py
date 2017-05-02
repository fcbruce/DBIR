#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 01 May 2017 20:14:00
#
#

from keras.applications.vgg16 import VGG16, preprocess_input

from FeatureGenerator import FeatureGenerator

class VGG16FeatureGenerator(FeatureGenerator):

    def __init__(self, weights='imagenet'):
        FeatureGenerator.__init__(self, VGG16, (224, 224), preprocess_input, weights)


