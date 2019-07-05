# Face Detector

- Face recognition from a video using [OpenCV](https://pypi.org/project/opencv-python/)
- Using Qt ([Qt for Python](https://doc.qt.io/qtforpython/index.html)) for displaying

---

1. [Environment](#Environment)
   1. [Software](#Software)
1. [Todo & Issues](#Todo--Issues)
   1. [Closing OpenGL window](#Closing-OpenGL-window)
1. [Installation](#Installation)
1. [Configuration](#Configuration)
1. [Usage](#Usage)

---

## Environment

### Software

- Python 3.7.3
- Ubuntu 18.04.2
- Arch Linux x86_64 (2019/7/4)
- Windows 10 1903

## Todo & Issues

- [ ] Add selecting camera resolution
- Try various algorythms
    - [ ] YOLOv3
    - [ ] [M2Det](https://qijiezhao.github.io/imgs/m2det.pdf)
    - [ ] [SSD](https://arxiv.org/pdf/1512.02325.pdf)
- [x] OpenGL support for displaying to improve rendering performance
- [x] OpenCV cascade classifier
    - [x] [Video](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html)
        - [x] Reading from the file
        - [x] Reading from the webcam
    - [x] [Picture](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection)

### Closing OpenGL window

- It dumps core when closing window includes OpenGL widget

```
[xcb] Unknown request in queue while appending request
[xcb] Most likely this is a multi-threaded client and XInitThreads has not been called
[xcb] Aborting, sorry about that.
python: ../../src/xcb_io.c:151: append_pending_request: Assertion `!xcb_xlib_unknown_req_pending' failed.
```

## Installation

```bash
# Common modules
$ pip install opencv-python python-dotenv PySide2
# Make sure the version number can be displayed
$ python -c "import cv2; print(cv2.__version__)"
4.1.0

# dark_recognizer.py
$ pip install Cython
# Install DarkFlow
$ git clone git@github.com:thtrieu/darkflow.git
$ cd darkflow
$ python setup.py build_ext --inplace
$ pip install .
# Download and place YOLOv2 weights file
$ mkdir weights
$ wget https://pjreddie.com/media/files/yolov2-tiny.weights -O weights/yolov2-tiny.weights
```

## Configuration

- Create `.env` file and add following settings
- To see available OpenCV classifiers, run `$ ls $(python -c 'import cv2; print(cv2.data.haarcascades)') | grep xml`

```bash
# OpenCV classifier type
CASCADE_CLASSIFIER_TYPE = 'haarcascade_frontalface_default.xml'

# Path to YOLOv2 classifier
YOLO_WEIGHTS = 'weights/yolov2.weights'
YOLO_CFG = 'cfg/yolov2.cfg'
```

## Usage

- `-h` option for help

```bash
$ python face_recognizer.py images/sample.jpg

# Start your computer's webcam if no file passed
$ python v_face_recognizer.py -i images/Walking.mp4
```

[tf]: https://www.tensorflow.org/
[pydl]: https://www.python.org/downloads/release/python-367/
[opencv]: https://opencv.org/releases.html
