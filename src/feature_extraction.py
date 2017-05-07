#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 01 May 2017 20:53:07
#
#

import os
import json

from VGG16FeatureGenerator import VGG16FeatureGenerator
from CacheLoader import CacheLoader

image_folder = '../data/256_ObjectCategories/'

if __name__ == '__main__':

    cache = CacheLoader()

    for subfolder in os.listdir(image_folder):
        image_paths = [os.path.join(image_folder, subfolder, image) for image in os.listdir(os.path.join(image_folder, subfolder)) if image.endswith('.jpg') and not cache.exists(image)]

        generator = VGG16FeatureGenerator()
        images =  [generator.load_img(image) for image in image_paths]
        images = generator.img_preprocess(images)
        features = generator.generate_feature(images)
        for path, feature in zip(image_paths, features):
            cache.set(os.path.basename(path), json.dumps(feature.tolist()))
        print subfolder, "done!"
