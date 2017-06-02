#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 23 May 2017 22:32:41
#
#

import cv2
import sys

if __name__ == '__main__':

    path = sys.argv[1]
    img = cv2.imread(path)

    sift = cv2.SIFT()
    #sift = cv2.xfeatures2d.SIFT_create()
    features = sift.detect(img)
    for feature in features:
        cv2.circle(img, (int(feature.pt[0]), int(feature.pt[1])), 1, (255, 255, 0), -1)

    # img_sift = cv2.drawKeypoints(img, features)

    cv2.imshow('SIFT', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




