import cv2
from PySide2 import QtCore, QtGui, QtWidgets
from queue import Queue
import time

from modules.image_recognizer import draw_rectangles, recognize_face


def cv2pixmap(cvimage):
    cvimage = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB)
    height, width, dim = cvimage.shape

    return QtGui.QPixmap.fromImage(QtGui.QImage(cvimage.data, width, height, dim * width, QtGui.QImage.Format_RGB888))


# Non-OpenGL image displaying widget
class ImageArea(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # TODO: OpenGL implementation
        self.initializeGL()

    def initializeGL(self):
        print('Initializing image area ...')
        self.view = QtWidgets.QGraphicsView()
        self.view.setupViewport(self)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.SmartViewportUpdate)
        self.scene = QtWidgets.QGraphicsScene()

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.view)
        self.setLayout(layout)

    def setCVImage(self, cvimage):
        items = self.scene.items()
        if len(items) > 3:
            self.scene.removeItem(items[-1])

        self.scene.addItem(QtWidgets.QGraphicsPixmapItem(cv2pixmap(cvimage)))
        self.view.setScene(self.scene)


class VideoArea(ImageArea):
    def __init__(self, video_path=None):
        self.video = cv2.VideoCapture(video_path)
        self.orig_fps = self.video.get(cv2.CAP_PROP_FPS)
        self.frames = Queue(maxsize=32)

        self.stopped = False

        super().__init__()

    num_frames = 0

    def update(self):
        if self.stopped:
            return

        self.setCVImage(self.frames.get())

    def show(self):
        orig_size = (int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.setGeometry(0, 0, orig_size[0], orig_size[1])

        loader = QtCore.QTimer(self.view)
        loader.timeout.connect(self.load_frame)
        loader.start()

        updater = QtCore.QTimer(self.view)
        updater.timeout.connect(self.update)
        updater.start()

        self.start_time = time.time()
        fps_counter = QtCore.QTimer(self.view)
        fps_counter.timeout.connect(self.get_fps)
        # mspf: milliseconds per frame
        fps_counter.start((1 / self.orig_fps) * 1000)

        super().show()

    def load_frame(self):
        ret, frame = self.video.read()

        if ret:
            self.num_frames += 1
            faces = recognize_face(frame)
            print('found faces:', len(faces))
            draw_rectangles(frame, faces)
            # return frame
            self.frames.put(frame)
        else:
            self.stop()
            return

    def stop(self):
        self.video.release()
        self.stopped = True

    def get_fps(self):
        if self.stopped:
            return

        elapsed_time = time.time() - self.start_time
        fps = self.num_frames / (time.time() - self.start_time)
        self.setWindowTitle("Elapsed time: {:.2f} sec, frame count: {} ({:.2f} FPS, {:.2f} % speed)".format(
            elapsed_time,
            self.num_frames,
            fps,
            (fps / self.orig_fps) * 100
        ))
