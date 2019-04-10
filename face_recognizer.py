import argparse
from pathlib import Path

import cv2
import matplotlib.pyplot as plt

import settings
from modules.image_recognizer import draw_rectangles, recognize_face

cascade = cv2.CascadeClassifier(str(settings.CASCADE_CLASSIFIER_PATH))


def main():
    parser = argparse.ArgumentParser(description='画像から顔を認識するスクリプト')
    parser.add_argument('input', type=str, help='入力ファイルのパス')
    parser.add_argument('-o', '--output', type=str, help='出力ファイルのパス（デフォルト：なし（保存しない））')
    args = parser.parse_args()

    img = cv2.imread(str(Path(args.input)))
    faces = recognize_face(img, scale_factor=1.1, min_size=50)
    print('found faces:', len(faces))
    draw_rectangles(img, faces)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if args.output:
        plt.savefig(str(Path(args.output)))

    plt.show()


if __name__ == '__main__':
    main()
