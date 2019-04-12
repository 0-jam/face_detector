# Face Detector

- Face recognition from a video using [OpenCV](https://pypi.org/project/opencv-python/)
- Using Qt ([Qt for Python](https://doc.qt.io/qtforpython/index.html)) for displaying

---

1. [Environment](#environment)
   1. [Software](#software)
1. [Todo & Issues](#todo--issues)
1. [Installation](#installation)
1. [Configuration](#configuration)
1. [Usage](#usage)

---

## Environment

### Software

- Python 3.7.3
- Ubuntu 18.04.2

## Todo & Issues

- [ ] OpenGL support for displaying to improve rendering performance
- [ ] Got `Segmentation Fault` when closed window (Linux only?)
- [x] Pure OpenCV
    - [x] [Video](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html)
        - [x] Reading from the file
        - [x] Reading from the webcam
    - [x] [Picture](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection)

## Installation

```bash
# video_recognizer.py
$ pip install opencv-python python-dotenv numpy PySide2
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

```
# Path to OpenCV classifier
# <directory which OpenCV installed>/opencv/sources/data
# Backslashes (\) needs to be escaped
CASCADE_CLASSIFIER_PATH = "path\\to\\classifier.xml"
```

## Usage

- `-h` option for help

```ps1
> python .\face_recognizer.py path/to/image
# Start your computer's webcam if no file passed
# If there is no available webcams, script will do nothing and stop
> python .\video_recognizer.py -i images/Walking.mp4
```

[tf]: https://www.tensorflow.org/
[pydl]: https://www.python.org/downloads/release/python-367/
[opencv]: https://opencv.org/releases.html
