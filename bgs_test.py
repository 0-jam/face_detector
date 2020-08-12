import cv2
import numpy as np

from modules.resolution import get_video_size


def main():
    video = cv2.VideoCapture(0)
    bgs = cv2.createBackgroundSubtractorMOG2()

    video_width, video_height = get_video_size(video)
    total_pixel = video_width * video_height

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

            print('difference: {:5d} / {} ({:.2f}%)'.format(frame_diff, total_pixel, (frame_diff / total_pixel) * 100), end='\r', flush=True)

            cv2.waitKey(1)
    except KeyboardInterrupt:
        print()
    finally:
        cv2.destroyAllWindows()
        video.release()

    print("done")


if __name__ == '__main__':
    main()
