import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

CASCADE_CLASSIFIER_PATH = Path(os.environ.get("CASCADE_CLASSIFIER_PATH"))
