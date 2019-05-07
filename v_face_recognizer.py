import argparse

from PySide2.QtWidgets import QApplication

from modules.qt_image_area import VideoArea


def main():
    parser = argparse.ArgumentParser(description='Recognize faces from an video file')
    parser.add_argument('-i', '--input', type=str, help='Input file (default: Webcam on your computer)')
    parser.add_argument('-o', '--output', type=str, help='Output file (default: None)')
    args = parser.parse_args()

    if args.input:
        video = args.input
    else:
        video = 0

    app = QApplication([])

    window = VideoArea(video, args.output)
    window.show()

    app.exit(app.exec_())


if __name__ == '__main__':
    main()
