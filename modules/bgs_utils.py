import cv2
import numpy as np
import tqdm

HISTSIZE = 30 * 60 * 60
bgs = cv2.createBackgroundSubtractorMOG2(history=HISTSIZE)


def apply_bgs(frame):
    fg_mask = bgs.apply(frame)
    _, th_fg_mask = cv2.threshold(fg_mask, 127, 255, cv2.THRESH_BINARY_INV)

    return th_fg_mask


def calc_difference(frame):
    return np.count_nonzero(frame == 0)


# Fill history with the current frame
# It takes a long time
def calibrate_bgs(frame):
    for _ in tqdm.tqdm(range(HISTSIZE), desc='calibrating bgs ...'):
        apply_bgs(frame)
