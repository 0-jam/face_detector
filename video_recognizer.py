import argparse
from pathlib import Path

from modules.qt_face_recognizer import FaceRecognizer
from PySide2 import QtWidgets


def main():
    parser = argparse.ArgumentParser(description='Recognize faces from a video file or webcam')
    parser.add_argument('-i', '--input', type=str, help='Input file (default: Webcam on your computer)')
    parser.add_argument('-o', '--output', type=str, default='', help='Output file (default: none)')
    args = parser.parse_args()

    if args.input:
        video = str(Path(args.input))
    else:
        video = 0

    if args.output:
        out_path = str(Path(args.output))
    else:
        out_path = ''

    app = QtWidgets.QApplication([])
    recognizer = FaceRecognizer(video, out_path=out_path)
    recognizer.stream()
    app.exit(app.exec_())


if __name__ == '__main__':
    main()
