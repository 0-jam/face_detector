import cv2

MAX_WIDTH = 3840
MAX_HEIGHT = 2160


# Get (width, height) from the OpenCV VideoCapture instance
def get_video_size(cvvideo):
    return (int(cvvideo.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cvvideo.get(cv2.CAP_PROP_FRAME_HEIGHT)))


# Get maximum resolution of the specified webcam
def get_webcam_resolution(device_num=0):
    camera = cv2.VideoCapture(device_num)

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, MAX_WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, MAX_HEIGHT)

    resolution = get_video_size(camera)

    camera.release()

    return resolution
