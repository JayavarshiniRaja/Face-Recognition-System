import numpy as np
import pywt
import cv2


def w2d(image, mode='haar', level=1):
    array = image
    array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    array = np.float32(array)
    array /= 255

    coeff = pywt.wavedec2(array, mode, level=level)
    new_coeff = list(coeff)
    new_coeff[0] *= 0

    new_array = pywt.waverec2(new_coeff, mode);
    new_array *= 255;
    new_array = np.uint8(new_array)

    return new_array

