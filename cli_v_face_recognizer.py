import argparse
import json
import time
from pathlib import Path

import cv2

from modules.cv_dark_recognizer import recognize_face
# from modules.dark_recognizer import recognize_face


def main():
    parser = argparse.ArgumentParser(description='Recognize objects from a video file without showing any images')
    parser.add_argument('-i', '--input', type=str, help='Input file (default: Webcam on your computer)')
    parser.add_argument('--output', '-o', type=str, help='Output file (default: none)')
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
    objects = []
    while vc.isOpened():
        ret, frame = vc.read()

        if ret:
            num_frames += 1
            objects.append(recognize_face(frame))
            elapsed_time = time.time() - start_time
            fps = num_frames / elapsed_time
            print('Found objects: {}, Elapsed time: {:.2f} sec, frame count: {} ({:.2f} FPS, {:.2f} % speed)'.format(
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

    # BUG: It should not working when using webcam
    out_path = args.output
    if out_path is not None:
        with Path(out_path).open('w') as out_json:
            out_json.write(json.dumps(objects, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
