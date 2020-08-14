import cv2
import numpy as np

bgs = cv2.createBackgroundSubtractorMOG2()


def apply_bgs(frame):
    fg_mask = bgs.apply(frame)
    _, th_fg_mask = cv2.threshold(fg_mask, 127, 255, cv2.THRESH_BINARY_INV)

    return th_fg_mask


def calc_difference(frame):
    return np.count_nonzero(frame == 0)
