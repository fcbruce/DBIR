#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 22 May 2017 11:09:18
#
#

from keras.applications.resnet50 import ResNet50
from keras.applications.xception import Xception
from keras.applications.inception_v3 import InceptionV3
from keras.applications.vgg16 import VGG16
from keras.utils.vis_utils import plot_model

vgg16 = VGG16(weights='imagenet', include_top=False, pooling='max')
plot_model(vgg16, to_file='vgg16_model.png')

res50 = ResNet50(weights='imagenet', include_top=False, pooling='avg')
plot_model(res50, to_file='res50_model.png')

xception = Xception(weights='imagenet', include_top=False, pooling='avg')
plot_model(xception, to_file='xception_model.png')

inception_v3 = InceptionV3(weights='imagenet', include_top=False, pooling='avg')
plot_model(inception_v3, to_file='inceptionv3_model.png')
