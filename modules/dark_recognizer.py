import cv2

import settings
from darkflow.net.build import TFNet

options = {'model': str(settings.YOLO_CFG), 'load': str(settings.YOLO_WEIGHTS), 'threshold': 0.1, 'gpu': 0.5}
tfnet = TFNet(options)


# 引数imgで与えられた画像から物体を検出
# 返り値はJSON形式
def recognize_face(img):
    return tfnet.return_predict(img)


# 物体と認識された部分objectsを長方形で囲む
# 物体が認識されなければ何も描画されない
def draw_rectangles(img, objects):
    for obj in objects:
        topleft = obj["topleft"]
        bottomright = obj["bottomright"]
        cv2.rectangle(
            img,
            (topleft["x"], topleft["y"]),
            (bottomright["x"], bottomright["y"]),
            (int(255 * obj["confidence"]), 0, 0),
            2
        )
