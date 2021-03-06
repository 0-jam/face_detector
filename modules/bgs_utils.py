import cv2
import numpy as np
import tqdm


class BGSubtractor(object):
    def __init__(self):
        self.histsize = 30 * 60 * 30
        self.reset_bgs()

    def apply_bgs(self, frame):
        fg_mask = self.bgs.apply(frame)
        _, th_fg_mask = cv2.threshold(fg_mask, cv2.THRESH_OTSU, 255, cv2.THRESH_BINARY_INV)

        return fg_mask, th_fg_mask

    @staticmethod
    def calc_difference(frame):
        return np.count_nonzero(frame == 255)

    # Fill history with the current frame
    # It takes a long time
    def calibrate_bgs(self, frame):
        for _ in tqdm.tqdm(range(self.histsize), desc='calibrating bgs ...'):
            self.apply_bgs(frame)

    def reset_bgs(self):
        self.bgs = cv2.createBackgroundSubtractorMOG2(history=self.histsize)
