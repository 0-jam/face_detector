from pathlib import Path

import cv2
import numpy as np

import settings

cv2.ocl.useOpenCL()

yolo_net = cv2.dnn.readNetFromDarknet('cfg/yolov3.cfg', 'weights/yolov3.weights')
yolo_net.setPreferableTarget(cv2.dnn.DNN_TARGET_OPENCL)

labels = Path('yolo_labels/labels.txt').open().read().split('\n')
layer_names = yolo_net.getLayerNames()
output_layer_names = [layer_names[i[0] - 1] for i in yolo_net.getUnconnectedOutLayers()]


def recognize_face(img):
    img_blob = cv2.dnn.blobFromImage(img, scalefactor=1.0/255.0, size=(416, 416), swapRB=True)
    img_h, img_w = img.shape[:2]

    yolo_net.setInput(img_blob)
    outputs = yolo_net.forward(output_layer_names)

    label_ids = []
    boxes = []
    confidences = []
    for output in outputs:
        for pred in output:
            scores = pred[5:]
            label_index = np.argmax(scores)
            confidence = scores[label_index]
            # Remove low confidence (= probability) objects
            if confidence > 0.7:
                label_ids.append(label_index)
                confidences.append(float(confidence))

                box = pred[0:4] * np.array([img_w, img_h, img_w, img_h])
                center_x, center_y, width, height = box.astype('int')
                face_x = int(center_x - (width / 2))
                face_y = int(center_y - (height / 2))

                boxes.append([face_x, face_y, int(width), int(height)])

    # Apply Non-Maximum Suppression to detected objects
    nms_box_ids = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3).flatten()

    return [{'label': labels[label_ids[i]], 'area': boxes[i], 'confidence': confidences[i]} for i in nms_box_ids]


# Render nothing if no objects recognized
def draw_rectangles(img, objects):
    for obj in objects:
        topleft_x, topleft_y = obj['area'][0], obj['area'][1]
        bottomright_x, bottomright_y = topleft_x + obj['area'][2], topleft_y + obj['area'][3]
        cv2.rectangle(
            img,
            (topleft_x, topleft_y),
            (bottomright_x, bottomright_y),
            (int(255 * obj['confidence']), 0, 0),
            2
        )
