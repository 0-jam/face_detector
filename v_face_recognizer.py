import argparse
from pathlib import Path

from PySide2.QtWidgets import QApplication

from modules.qt_image_area import VideoArea


def main():
    parser = argparse.ArgumentParser(description='Recognize faces from an video file')
    parser.add_argument('input', type=str, help='Input file')
    args = parser.parse_args()

    app = QApplication([])

    window = VideoArea(str(Path(args.input)))
    window.show()

    app.exit(app.exec_())


if __name__ == '__main__':
    main()
