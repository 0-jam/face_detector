import cv2

import settings
from modules import darknet

from tempfile import NamedTemporaryFile

net = darknet.load_net(bytes(settings.YOLO_CFG, 'utf-8'), bytes(settings.YOLO_WEIGHTS, 'utf-8'), 0)
meta = darknet.load_meta(bytes(settings.YOLO_DATA, 'utf-8'))


# Detect faces from file
def recognize_face_file(img_path):
    faces = darknet.detect(net, meta, bytes(img_path, 'utf-8'))

    return [{
        'label': face[0].decode(),
        'confidence': face[1],
        'position': face[2],
    } for face in faces]


# Detect faces from img
def recognize_face(img):
    # Create a temporary file to pass detect() function
    with NamedTemporaryFile(suffix='.jpg') as tmpimg:
        tmpname = tmpimg.name
        cv2.imwrite(tmpname, img)
        faces = darknet.detect(net, meta, bytes(tmpname, 'utf-8'))

    return [{
        'label': face[0].decode(),
        'confidence': face[1],
        'position': face[2],
    } for face in faces]


# Render nothing if no faces recognized
def draw_rectangles(img, faces):
    for face in faces:
        center_x, center_y, width, height = face['position']
        topleft_x = int(center_x - width / 2)
        topleft_y = int(center_y - height / 2)
        bottomright_x = int(topleft_x + width)
        bottomright_y = int(topleft_y + height)
        cv2.rectangle(img, (topleft_x, topleft_y), (bottomright_x, bottomright_y), (255, 0, 0), 2)
