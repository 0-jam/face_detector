import argparse
import json
import time
from pathlib import Path

import cv2

from modules.cv_dark_recognizer import recognize_face


def main():
    parser = argparse.ArgumentParser(description='Recognize objects using pre-trained Darknet model')
    parser.add_argument('input', type=str, help='Input file')
    parser.add_argument('--output', '-o', type=str, help='Output file (default: none)')
    args = parser.parse_args()

    img = cv2.imread(str(Path(args.input)))

    start_time = time.time()
    faces = recognize_face(img)
    elapsed_time = time.time() - start_time
    print('Found objects: {}, Elapsed time: {:.2f} sec'.format(len(faces), elapsed_time))

    out_path = args.output
    if out_path is not None:
        with Path(out_path).open('w') as out_json:
            out_json.write(json.dumps(faces, ensure_ascii=False))


if __name__ == '__main__':
    main()
