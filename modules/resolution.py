import cv2

MAX_W = 3840
MAX_H = 2160


def get_webcam_resolution(device_num=0):
    camera = cv2.VideoCapture(device_num)

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, MAX_W)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, MAX_H)

    resolution = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    camera.release()

    return resolution
