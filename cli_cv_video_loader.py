import argparse
import time

import cv2
from modules.resolution import set_webcam_resolution


def main():
    parser = argparse.ArgumentParser(description='Just load frames from the camera without doing anything')
    args = parser.parse_args()

    video = 0

    vc = cv2.VideoCapture(video, apiPreference=cv2.CAP_V4L)
    set_webcam_resolution(vc, width=640, height=480, fps=30)

    num_frames = 0
    orig_fps = vc.get(cv2.CAP_PROP_FPS)
    start_time = time.time()

    while vc.isOpened():
        ret, _ = vc.read()

        if ret:
            num_frames += 1
            fps = num_frames / (time.time() - start_time)
            print('{:.2f} FPS, {:.2f} % speed'.format(
                fps,
                (fps / orig_fps) * 100
            ), end='\r')
        else:
            vc.release()
            print('')
            break


if __name__ == '__main__':
    main()
