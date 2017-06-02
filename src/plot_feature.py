#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 22 May 2017 14:41:35
#
#

import sys

from VGG16FeatureGenerator import VGG16FeatureGenerator
from keras.applications.vgg16 import VGG16, preprocess_input as vgg16_preprocess
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    img_path = sys.argv[1]
    if not img_path:
        exit(1)

    model = VGG16(weights='imagenet', include_top=False)

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = vgg16_preprocess(x)

    features = model.predict(x)

    print features.shape
    features = np.squeeze(features, axis=0)
    print features
    print features.shape
    print features[:, :, -1]
    print features[:, :, -1].shape
    plt.imshow(features[:, :, -1])


