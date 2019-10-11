import argparse
import csv
import time
from pathlib import Path

import cv2

from modules.cv_dark_recognizer import recognize_face


def main():
    parser = argparse.ArgumentParser(description='Recognize objects from a video file without showing any images')
    parser.add_argument('--input', '-i', type=str, help='Input file (default: Webcam on your computer)')
    parser.add_argument('--output', '-o', type=str, default='faces.csv', help='Output file (default: faces.csv)')
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
    with Path(args.output).open('w') as out_csv:
        writer = csv.DictWriter(out_csv, fieldnames=['frame', 'label', 'topleft_x', 'topleft_y', 'width', 'height', 'confidence'])
        writer.writeheader()

        while vc.isOpened():
            ret, frame = vc.read()

            if ret:
                num_frames += 1
                faces = recognize_face(frame)
                elapsed_time = time.time() - start_time
                fps = num_frames / elapsed_time
                print('Found objects: {}, Elapsed time: {:.2f} sec, frame count: {} ({:.2f} FPS, {:.2f} % speed)'.format(
                    len(faces),
                    elapsed_time,
                    num_frames,
                    fps,
                    (fps / orig_fps) * 100
                ), end='\r')

                # Add frame count in information of recognized objects
                [face.update({'frame': num_frames}) for face in faces]
                writer.writerows(faces)
            else:
                vc.release()
                print('')
                break


if __name__ == '__main__':
    main()
