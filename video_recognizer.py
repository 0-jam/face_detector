import argparse
import sys
from pathlib import Path

from modules.qt_face_recognizer import FaceRecognizer
from PyQt5 import QtWidgets


def main():
    parser = argparse.ArgumentParser(description="動画ファイルまたはWebカメラから顔を認識するスクリプト")
    parser.add_argument("-i", "--input", type=str, help="入力ファイルのパス（デフォルト：端末のWebカメラ）")
    parser.add_argument("-o", "--output", type=str, default="", help="出力ファイルのパス（デフォルト：保存しない）")
    args = parser.parse_args()

    if args.input:
        video = str(Path(args.input))
    else:
        video = 0

    if args.output:
        out_path = str(Path(args.output))
    else:
        out_path = ""

    app = QtWidgets.QApplication([])
    recognizer = FaceRecognizer(video, out_path=out_path)
    recognizer.stream()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
