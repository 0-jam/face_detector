import argparse
from pathlib import Path

import cv2
from PySide2 import QtWidgets

from modules.image_recognizer import draw_rectangles, recognize_face
from modules.qt_image_recognizer import ImageArea


def main():
    parser = argparse.ArgumentParser(description='Recognize faces from an image file')
    parser.add_argument('input', type=str, help='Input file')
    parser.add_argument('--output', '-o', type=str, help='Output file (default: none)')
    args = parser.parse_args()

    img = cv2.imread(str(Path(args.input)))
    faces = recognize_face(img, scale_factor=1.1, min_size=50)
    print('found faces:', len(faces))
    draw_rectangles(img, faces)

    if args.output:
        print('Saving image ...')
        cv2.imwrite(args.output, img)

    app = QtWidgets.QApplication()

    window = ImageArea()
    window.setCVImage(img)
    window.show()

    app.exit(app.exec_())


if __name__ == '__main__':
    main()
