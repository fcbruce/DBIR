
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 01 May 2017 20:53:07
#
#

import os

from VGG16FeatureGenerator import VGG16FeatureGenerator

image_folder = '../data/256_ObjectCategories/'


for subfolder in os.listdir(image_folder):
    images = [os.path.join(image_folder, subfolder, image) for image in os.listdir(os.path.join(image_folder, subfolder)) if image.endswith('.jpg')]

    generator = VGG16FeatureGenerator()
    images =  [generator.load_img(image) for image in images]
    print len(images)
    images = generator.img_preprocess(images)
    print images.shape
    print generator.generate_feature(images).shape
