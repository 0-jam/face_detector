from collections import deque
from statistics import mean

import cv2

from modules.bgs_utils import apply_bgs, calc_difference
from modules.resolution import get_video_size


def main():
    video = cv2.VideoCapture(0)

    video_width, video_height = get_video_size(video)
    total_pixel = video_width * video_height
    avg_diff = 0
    diffs = deque(maxlen=int(video.get(cv2.CAP_PROP_FPS)) * 2)

    try:
        while True:
            ret, frame = video.read()
            if ret is None:
                break

            th_fg_mask = apply_bgs(frame)

            cv2.imshow('Actual Image', frame)
            cv2.imshow('FG Mask (applied threshold)', th_fg_mask)

            frame_diff = calc_difference(th_fg_mask)

            diffs.append(frame_diff)
            avg_diff = mean(diffs)

            print('difference: {:5d} / {:9d} ({:.2f}%), average: {:.3f}'.format(
                frame_diff,
                total_pixel,
                (frame_diff / total_pixel) * 100,
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
