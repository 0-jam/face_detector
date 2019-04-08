import argparse
from pathlib import Path

import cv2
import matplotlib.pyplot as plt

import settings
from darkflow.net.build import TFNet

options = {'model': str(settings.YOLO_CFG), 'load': str(settings.YOLO_WEIGHTS), 'threshold': 0.1, 'gpu': 0.5}
tfnet = TFNet(options)


# 引数imgで与えられた画像から物体を検出
# 返り値はJSON形式
def recognize_face(img, scale_factor=2):
    orig_height, orig_width = img.shape[:2]
    size = (int(orig_height / scale_factor), int(orig_width / scale_factor))
    cv2.resize(img, size)
    return tfnet.return_predict(img)


# 物体と認識された部分objectsを長方形で囲む
# 物体が認識されなければ何も描画されない
def draw_rectangles(img, objects):
    for obj in objects:
        confidence = obj["confidence"]
        topleft = obj["topleft"]
        bottomright = obj["bottomright"]
        cv2.rectangle(
            img,
            (topleft["x"], topleft["y"]),
            (bottomright["x"], bottomright["y"]),
            (int(255 * confidence), 0, 0),
            2
        )


def main():
    parser = argparse.ArgumentParser(description="画像から顔を認識するスクリプト")
    parser.add_argument("input", type=str, help="入力ファイルのパス")
    parser.add_argument("-o", "--output", type=str, help="出力ファイルのパス（デフォルト：なし（保存しない））")
    args = parser.parse_args()

    img = cv2.imread(str(Path(args.input)))
    result = recognize_face(img)
    draw_rectangles(img, result)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    print(result)
    plt.show()


if __name__ == '__main__':
    main()
