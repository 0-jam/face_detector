# Face Detector

- Face recognition from a video using [OpenCV](https://pypi.org/project/opencv-python/)
- Using Qt ([Qt for Python](https://doc.qt.io/qtforpython/index.html)) for displaying

---

1. [Environment](#environment)
   1. [Software](#software)
1. [Todo & Issues](#todo--issues)
   1. [Closing OpenGL window](#closing-opengl-window)
1. [Installation](#installation)
1. [Configuration](#configuration)
1. [Usage](#usage)

---

## Environment

### Software

- Python 3.7.4
- Arch Linux x86_64 (2019/10/4)
- Windows 10 1903
- TensorFlow < 2.0 (for Darkflow object recognizer)
- OpenCV 4.1.1

## Todo & Issues

- [ ] JSON output for webcam object detection
- [ ] Add selecting camera resolution
- [x] Separate OpenCV video capture from Qt GUI
- Try various algorythms
    - [x] YOLOv3
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
$ pip install -U --user -r requirements.txt
# Make sure the version number can be displayed
$ python -c "import cv2; print(cv2.__version__)"
4.1.1

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

# Maximum webcam resolution for video object recognizer
# It is not affected to loading video files
MAX_CAMERA_RES_H = 1920
MAX_CAMERA_RES_V = 1080

# Specify OpenCL device for OpenCV and config directory
OPENCV_OPENCL_DEVICE=:dgpu
OPENCV_OCL4DNN_CONFIG_PATH='/home/<user>/.cache/opencv/4.1/opencl_cache'
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

[tf]: https://www.tensorflow.org/
[pydl]: https://www.python.org/downloads/release/python-367/
[opencv]: https://opencv.org/releases.html
