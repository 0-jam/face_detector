import argparse
import time
from pathlib import Path

import cv2

from modules.dark_recognizer import recognize_face


def main():
    parser = argparse.ArgumentParser(description="Recognize objects from an image file without showing any images")
    parser.add_argument('input', type=str, help='Input file')
    args = parser.parse_args()

    img = cv2.imread(str(Path(args.input)))

    start_time = time.time()
    faces = recognize_face(img)
    elapsed_time = time.time() - start_time
    print('Found objects: {}, Elapsed time: {:.2f} sec'.format(len(faces), elapsed_time))


if __name__ == '__main__':
    main()
