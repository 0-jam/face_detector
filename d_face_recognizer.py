import argparse
from pathlib import Path

import cv2
from PySide2.QtWidgets import QApplication

from modules.dark_recognizer import draw_rectangles, recognize_face
from modules.qt_image_area import ImageArea


def main():
    parser = argparse.ArgumentParser(description="Recognize objects from an image file")
    parser.add_argument('input', type=str, help='Input file')
    parser.add_argument('--output', '-o', type=str, help='Output file (default: none)')
    args = parser.parse_args()

    img = cv2.imread(str(Path(args.input)))
    result = recognize_face(img)
    print(result)
    draw_rectangles(img, result)

    if args.output:
        print('Saving image ...')
        cv2.imwrite(args.output, img)

    app = QApplication([])

    window = ImageArea()
    window.setCVImage(img)
    window.show()

    app.exit(app.exec_())


if __name__ == '__main__':
    main()
