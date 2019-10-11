import os

from dotenv import load_dotenv

load_dotenv()

# FACE_API_KEY = os.environ.get('FACE_API_KEY')
CASCADE_CLASSIFIER_TYPE = os.environ.get('CASCADE_CLASSIFIER_TYPE')
YOLO_WEIGHTS = os.environ.get('YOLO_WEIGHTS')
YOLO_CFG = os.environ.get('YOLO_CFG')
YOLO_LABELS = os.environ.get('YOLO_LABELS')
