from collections import deque
from statistics import mean

import cv2
import numpy as np

from modules.resolution import get_video_size


def main():
    video = cv2.VideoCapture(0)
    bgs = cv2.createBackgroundSubtractorMOG2()

    video_width, video_height = get_video_size(video)
    total_pixel = video_width * video_height
    max_diff = 0
    min_diff = total_pixel
    avg_diff = 0
    diffs = deque(maxlen=int(video.get(cv2.CAP_PROP_FPS)) * 2)

    try:
        while True:
            ret, frame = video.read()
            if ret is None:
                break

            fg_mask = bgs.apply(frame)
            _, th_fg_mask = cv2.threshold(fg_mask, 127, 255, cv2.THRESH_BINARY_INV)

            cv2.imshow('Lepton Radiometry', frame)
            cv2.imshow('FG Mask', fg_mask)
            cv2.imshow('FG Mask (applied threshold)', th_fg_mask)

            frame_diff = np.count_nonzero(th_fg_mask == 0)

            diffs.append(frame_diff)
            avg_diff = mean(diffs)

            if frame_diff > max_diff:
                max_diff = frame_diff

            if frame_diff < min_diff:
                min_diff = frame_diff

            print('difference: {:5d} / {:9d} ({:.2f}%), max: {:9d}, min: {:9d}, average: {:.3f}'.format(
                frame_diff,
                total_pixel,
                (frame_diff / total_pixel) * 100,
                max_diff,
                min_diff,
                avg_diff,
            ), end='\r', flush=True)

            cv2.waitKey(1)
    except KeyboardInterrupt:
        print()
    finally:
        cv2.destroyAllWindows()
        video.release()

    print("done")


if __name__ == '__main__':
    main()
