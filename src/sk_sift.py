#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 23 May 2017 22:46:30
#
#

from skimage import data, io as skio
import sys

if __name__ == '__main__':

    path = sys.argv[1]
    features = skio.sift.load_sift(path)
    print features
