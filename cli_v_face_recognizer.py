import argparse

import cv2
import time

from modules.dark_recognizer import recognize_face
# from modules.image_recognizer import recognize_face


def main():
    parser = argparse.ArgumentParser(description='Recognize objects from an video file without showing any images')
    parser.add_argument('-i', '--input', type=str, help='Input file (default: Webcam on your computer)')
    args = parser.parse_args()

    if args.input:
        video = args.input
    else:
        video = 0

    vc = cv2.VideoCapture()
    vc.open(video)

    num_frames = 0
    orig_fps = vc.get(cv2.CAP_PROP_FPS)
    start_time = time.time()
    while vc.isOpened():
        ret, frame = vc.read()

        if ret:
            num_frames += 1
            objects = recognize_face(frame)
            elapsed_time = time.time() - start_time
            fps = num_frames / elapsed_time
            print("Found objects: {}, Elapsed time: {:.2f} sec, frame count: {} ({:.2f} FPS, {:.2f} % speed)".format(
                len(objects),
                elapsed_time,
                num_frames,
                fps,
                (fps / orig_fps) * 100
            ), end='\r')
        else:
            vc.release()
            print('')
            break


if __name__ == '__main__':
    main()
