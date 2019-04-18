import cv2
import settings

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + settings.CASCADE_CLASSIFIER_TYPE)


# Detect faces from img
# Raise scale_factor and min_size for faster detection (precision will be lowered)
def recognize_face(img, scale_factor=1.5, min_size=50):
    return cascade.detectMultiScale(
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
        scaleFactor=scale_factor,
        minSize=(min_size, min_size)
    )


# Render nothing if no faces recognized
def draw_rectangles(img, faces):
    for (face_x, face_y, width, height) in faces:
        cv2.rectangle(img, (face_x, face_y), (face_x + width, face_y + height), (255, 0, 0), 2)
