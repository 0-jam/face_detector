import os
from pathlib import Path

from dotenv import load_dotenv

# .envファイルを読む
load_dotenv()

FACE_API_KEY = os.environ.get('FACE_API_KEY')
CASCADE_CLASSIFIER_PATH = Path(os.environ.get('CASCADE_CLASSIFIER_PATH'))
YOLO_WEIGHTS = Path(os.environ.get('YOLO_WEIGHTS'))
YOLO_CFG = Path(os.environ.get('YOLO_CFG'))
