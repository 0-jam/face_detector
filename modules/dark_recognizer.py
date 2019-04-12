import cv2

import settings
from darkflow.net.build import TFNet

options = {'model': str(settings.YOLO_CFG), 'load': str(settings.YOLO_WEIGHTS), 'threshold': 0.1, 'gpu': 0.5}
tfnet = TFNet(options)


# Detect objects from img
# Results will be returned as JSON
def recognize_face(img):
    return tfnet.return_predict(img)


# Render nothing if no objects recognized
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
