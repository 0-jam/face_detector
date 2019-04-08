import time
from queue import Queue
from threading import Thread

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

from face_recognizer import draw_rectangles, recognize_face


class FaceRecognizer():
    def __init__(self, video, out_path=""):
        self.video = cv2.VideoCapture(video)
        self.orig_fps = self.video.get(cv2.CAP_PROP_FPS)
        self.orig_size = (int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        if out_path:
            self.out = cv2.VideoWriter(
                out_path,
                cv2.VideoWriter_fourcc(*'MJPG'),
                self.orig_fps,
                self.orig_size
            )
        else:
            self.out = None

        self.frames = Queue(maxsize=128)
        self.stopped = False

        frame_loader = Thread(target=self.load_frame, args=())
        frame_loader.daemon = True
        frame_loader.start()

    # 動画から顔を認識し、四角で囲んで処理済みフレームself.framesに追加
    def load_frame(self):
        start_time = time.time()
        while self.video.isOpened():
            if self.stopped:
                return

            if not self.frames.full():
                ret, frame = self.video.read()

                if ret:
                    faces = recognize_face(frame)
                    if len(faces) > 0:
                        draw_rectangles(frame, faces)

                    if self.out:
                        self.out.write(frame)

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    self.frames.put(frame)
                else:
                    self.stop()
                    orig_frames = self.video.get(cv2.CAP_PROP_FRAME_COUNT)
                    elapsed_time = time.time() - start_time
                    fps = orig_frames / elapsed_time
                    print('Video stopped')
                    print("{:.2f} sec taken for loading {} frames ({:.2f} FPS, {:.2f} % speed)".format(
                        elapsed_time,
                        int(orig_frames),
                        fps,
                        (fps / self.orig_fps) * 100
                    ))
                    return

    # 事前に処理されたフレームを画面に表示
    def stream(self):
        self.view = QtWidgets.QGraphicsView()
        self.view.setViewport(QtWidgets.QOpenGLWidget())
        self.view.setGeometry(0, 0, self.orig_size[0], self.orig_size[1])
        self.scene = QtWidgets.QGraphicsScene()
        self.update_frame()

        frame_updater = QtCore.QTimer(self.view)
        frame_updater.timeout.connect(self.update_frame)

        self.start_time = time.time()
        print("Original FPS:", self.orig_fps)
        # mspf: milliseconds per frame
        mspf = (1 / self.orig_fps) * 1000
        frame_updater.start()

        fps_counter = QtCore.QTimer(self.view)
        fps_counter.timeout.connect(self.get_fps)
        fps_counter.start(mspf)

        self.view.show()

    # 画面に表示する内容を更新
    num_frames = 0

    def update_frame(self):
        if not self.frame_buffered():
            return

        frame = self.get_frame()
        self.num_frames += 1

        height, width, dim = frame.shape
        bytes_per_line = dim * width

        self.image = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        self.item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(self.image))
        self.scene.addItem(self.item)

        # メモリ使用量削減のため、古いフレームを配列から削除
        items = self.scene.items()
        if len(items) > 4:
            self.scene.removeItem(items[-1])

        self.view.setScene(self.scene)

    def get_frame(self):
        return self.frames.get()

    def frame_buffered(self):
        return self.frames.qsize() > 0

    def stop(self):
        self.stopped = True

    # FPSを取得してウィンドウタイトルに表示
    def get_fps(self):
        if self.stopped:
            return

        elapsed_time = time.time() - self.start_time
        fps = self.num_frames / (time.time() - self.start_time)
        self.view.setWindowTitle("Elapsed time: {:.2f} sec, frame count: {} ({:.2f} FPS, {:.2f} % speed)".format(
            elapsed_time,
            self.num_frames,
            fps,
            (fps / self.orig_fps) * 100
        ))
