#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 01 May 2017 20:37:39
#
#
from keras.preprocessing import image
import numpy as np

class FeatureGenerator:

    def __init__(self, model, target_size, preprocess_input, weights='imagenet'):
        self.model = model(weights=weights, include_top=False, pooling='max')
        self.target_size = target_size
        self.preprocess_input = preprocess_input
    
    def load_img(self, img_path):
        img = image.load_img(img_path, target_size=self.target_size)
        img = image.img_to_array(img)
        return img

    def img_preprocess(self, imgs):
        
        imgs = np.array(imgs)
        print imgs.shape
        imgs = imgs[:, :, :, ::-1]
        print imgs.shape
        return self.preprocess_input(imgs)

    def generate_feature(self, imgs):

        return self.model.predict(imgs)
