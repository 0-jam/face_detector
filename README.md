# Face Detector

- Face recognition from a video using [OpenCV](https://pypi.org/project/opencv-python/)
- Using Qt ([Qt for Python](https://doc.qt.io/qtforpython/index.html)) for displaying

---

1. [Environment](#environment)
    1. [Software](#software)
    1. [Closing OpenGL window](#closing-opengl-window)
1. [Installation](#installation)
    1. [GNU/Linux](#gnulinux)
    1. [Windows](#windows)
    1. [Installing Darknet](#installing-darknet)
1. [Configuration](#configuration)
1. [Usage](#usage)

---

## Environment

### Software

- Python 3.8.3 **except GUI video recognizer**
    - GUI video recognizer works on Python 3.7.4 or earlier
- Arch Linux x86_64 (2020/06/11)
- OpenCV 4.2.0

### Closing OpenGL window

- It dumps core when closing window includes OpenGL widget

```
[xcb] Unknown request in queue while appending request
[xcb] Most likely this is a multi-threaded client and XInitThreads has not been called
[xcb] Aborting, sorry about that.
python: ../../src/xcb_io.c:151: append_pending_request: Assertion `!xcb_xlib_unknown_req_pending' failed.
```

## Installation

### GNU/Linux

```bash
# Common modules
$ pip install -U --user -r requirements.txt
# Make sure the version number can be displayed
$ python -c "import cv2; print(cv2.__version__)"
4.2.0
```

### Windows

```
> pip install -U pip
> pip install pipenv
> pipenv install --dev
```

### Installing Darknet

1. Clone [tiagoshibata/darknet](https://github.com/tiagoshibata/darknet) (Including fixes for OpenCV 4)
1. Move to cloned darknet directory
1. `$ make`
1. Return this project's root directory
1. Copy compiled `libdarknet.so` file to `<this project's root>/lib`

## Configuration

- Create `.env` file and add following settings
- To see available OpenCV classifiers, run `$ ls $(python -c 'import cv2; print(cv2.data.haarcascades)') | grep xml`

```bash
# OpenCV classifier type
CASCADE_CLASSIFIER_TYPE = 'haarcascade_frontalface_default.xml'

# Maximum webcam resolution for video object recognizer
# It does not affect loading video files
MAX_CAMERA_RES_H = 1920
MAX_CAMERA_RES_V = 1080

# Path to the pre-trained YOLOv3 model and labels
YOLO_CFG = 'cfg/yolov3-tiny.cfg'
YOLO_WEIGHTS = 'weights/yolov3-tiny.weights'
YOLO_LABELS = 'yolo_labels/labels.txt'
YOLO_DATA = 'data/coco.data'
```

## Usage

- `-h` option for help

```bash
# *_face_recognizer.py except (cli_)v_face_recognizer.py has the same usage
$ python face_recognizer.py images/sample.jpg

# Start your computer's webcam if no file passed
# cli_v_face_recognizer.py has the same usage
$ python v_face_recognizer.py -i images/sample.mp4
```
