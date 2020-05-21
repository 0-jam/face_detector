import cv2
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description='View OpenCV VideoCapture properties')
    parser.add_argument('input', type=str, help='Input video file or camera')
    args = parser.parse_args()

    video = args.input
    try:
        video = int(args.input)
    except ValueError:
        video = str(Path(args.input))

    vc = cv2.VideoCapture(video)
    print('FPS:', vc.get(cv2.CAP_PROP_FPS))
    print('Resolution (W x H):', vc.get(cv2.CAP_PROP_FRAME_WIDTH), vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
    vc.release()


if __name__ == "__main__":
    main()
