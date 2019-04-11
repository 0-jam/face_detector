# Face Detector

- [OpenCV](https://pypi.org/project/opencv-python/)を使った動画顔認識システム
- 表示にはQt ([Qt for Python](https://doc.qt.io/qtforpython/index.html)) を使用
    - Qtの描画の一部にOpenGLを使用

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

- [ ] ウィンドウ閉じたときにSegmentation Faultする（Linuxのみ？）
- [ ] 顔認識に別のモデルを使う
- [x] Pure OpenCVで実装
    - [x] [動画](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html)
        - [x] ファイル読み込み
        - [x] カメラ
    - [x] [静止画](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection)

## Installation

```bash
# video_recognizer.py
# 必要パッケージインストール
$ pip install opencv-python python-dotenv numpy PySide2
# バージョン番号が表示されればインストール成功
$ python -c "import cv2; print(cv2.__version__)"
4.0.1

# dark_recognizer.py
$ pip install Cython
$ git clone git@github.com:thtrieu/darkflow.git
$ cd darkflow
$ python setup.py build_ext --inplace
$ pip install .
$ mkdir weights
$ wget https://pjreddie.com/media/files/yolov2-tiny.weights -O weights/yolov2-tiny.weights
```

## Configuration

- `.env`ファイルを作成して以下を追記

```
# OpenCV分類器のパス
# <OpenCVをインストールしたディレクトリ>/opencv/sources/data
# バックスラッシュ（\, Windowsのパスの区切り文字）はエスケープの必要あり
CASCADE_CLASSIFIER_PATH = "path\\to\\classifier.xml"
```

## Usage

- `-h`オプションでヘルプが表示される

```ps1
> python .\face_recognizer.py <画像ファイルのパス>
# 入力ファイルを渡さなかった場合、端末のWebカメラが起動する
# Webカメラが無効な場合、何もせずに終了する
> python .\video_recognizer.py -i images/Walking.mp4
```

[tf]: https://www.tensorflow.org/
[pydl]: https://www.python.org/downloads/release/python-367/
[opencv]: https://opencv.org/releases.html
