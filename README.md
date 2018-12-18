# Face Detector

- [OpenCV](https://pypi.org/project/opencv-python/)を使った動画顔認識システム
- 静止画顔認識結果の表示にMatplotlibを、動画顔認識結果の表示にQtをそれぞれ使用
    - Qtの描画の一部にOpenGLを使用

---

1. [Environment](#environment)
   1. [Software](#software)
1. [Todo & Issues](#todo--issues)
1. [Installation (Windows)](#installation-windows)
1. [Configuration](#configuration)
1. [Usage](#usage)

---

## Environment

### Software

- Python >= 3.6.7
- Windows 10 1803
- Ubuntu 18.04.1

## Todo & Issues

- [ ] ウィンドウ閉じたときにSegmentation Faultする（Linuxのみ？）
- [ ] 顔認識に別のモデルを使う
- [x] Pure OpenCVで実装
    - [x] [動画](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html)
        - [x] ファイル読み込み
        - [x] カメラ
    - [x] [静止画](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection)

## Installation (Windows)

- [Python公式のダウンロードページ(3.6.7)][pydl]から"Windows x86-64 executable installer"をクリックしてダウンロード、ファイルを実行してインストール
- pathを通す（コマンドラインから実行できるようにする）
    1. 「システム環境変数の編集」（スタートメニューから"env"と検索すると出てくる）から「環境変数」
    1. 「ユーザー環境変数」の"Path"をクリックして選択→「編集」
    1. 「新規」→`C:\Users\<ユーザー名>\AppData\Local\Programs\Python\Python36\`
    1. 「新規」→`C:\Users\<ユーザー名>\AppData\Local\Programs\Python\Python36\Scripts\`
- OpenCVの[本体][opencv]

```ps1
# これが通ればインストール成功
> python -V
Python 3.6.7
# pipアップデート
> python -m pip install -U pip
# 必要パッケージインストール
> pip install opencv-python python-dotenv matplotlib numpy pyqt5
# バージョン番号が表示されればインストール成功
> python -c "import cv2; print(cv2.__version__)"
3.4.3
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
