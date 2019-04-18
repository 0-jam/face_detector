import cv2
from PySide2 import QtCore, QtGui, QtWidgets
from queue import Queue
import time

from modules.image_recognizer import draw_rectangles, recognize_face
# from modules.dark_recognizer import draw_rectangles, recognize_face


def cv2pixmap(cvimage):
    cvimage = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB)
    height, width, dim = cvimage.shape

    return QtGui.QPixmap.fromImage(QtGui.QImage(cvimage.data, width, height, dim * width, QtGui.QImage.Format_RGB888))


# Image displaying widget
class ImageArea(QtWidgets.QOpenGLWidget):
    def __init__(self):
        super().__init__()

        # Initialize viewport
        self.view = QtWidgets.QGraphicsView()
        self.view.setupViewport(self)
        self.view.setViewportUpdateMode(QtWidgets.QGraphicsView.SmartViewportUpdate)
        self.scene = QtWidgets.QGraphicsScene()

        # Placing viewport to the window
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.view)
        self.setLayout(layout)

    # OpenGLWidget's virtual functions
    # Actually do nothing
    def initializeGL(self):
        pass

    def paintGL(self):
        pass

    def resizeGL(self, w, h):
        # print('Resizing ...', w, h)
        self.view.setGeometry(0, 0, w, h)

    def setCVImage(self, cvimage):
        items = self.scene.items()
        if len(items) > 1:
            self.scene.removeItem(items[-1])

        self.scene.addItem(QtWidgets.QGraphicsPixmapItem(cv2pixmap(cvimage)))
        self.view.setScene(self.scene)


class VideoArea(ImageArea):
    def __init__(self, video_path=None):
        # Loading video
        self.video = cv2.VideoCapture(video_path)
        self.orig_fps = self.video.get(cv2.CAP_PROP_FPS)
        self.frames = Queue(maxsize=64)
        self.num_frames = 0

        super().__init__()

        # Initializing frame loader
        self.loader = QtCore.QTimer(self.view)
        self.loader.timeout.connect(self.load_frame)

        # Initializing viewport updater
        self.updater = QtCore.QTimer(self.view)
        self.updater.timeout.connect(self.update)

        # Initializing FPS getter
        self.fps_counter = QtCore.QTimer(self.view)
        self.fps_counter.timeout.connect(self.show_fps)

    def closeEvent(self, event):
        self.stop_video()
        self.stop_render()

    def show(self):
        # Set window size
        orig_size = (int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.setGeometry(0, 0, orig_size[0], orig_size[1])

        self.loader.start()
        self.updater.start()

        self.start_time = time.time()
        self.fps_counter.start((1 / self.orig_fps) * 1000)

        super().show()

    def load_frame(self):
        ret, frame = self.video.read()

        if ret:
            self.num_frames += 1

            faces = recognize_face(frame)
            draw_rectangles(frame, faces)
            self.frames.put(frame)
        else:
            self.stop_video()
            return

    def update(self):
        if not self.frames.qsize() > 0:
            self.stop_render()
            return

        self.setCVImage(self.frames.get())

    def frame_buffered(self):
        return self.frames.qsize() > 0

    def stop_video(self):
        print('Video stopped')
        print(self.get_fps())

        self.video.release()
        self.loader.stop()

    def stop_render(self):
        print('Rendering stopped')
        print(self.get_fps())

        self.updater.stop()
        self.fps_counter.stop()

    def get_fps(self):
        elapsed_time = time.time() - self.start_time
        fps = self.num_frames / elapsed_time
        return "Elapsed time: {:.2f} sec, frame count: {} ({:.2f} FPS, {:.2f} % speed)".format(
            elapsed_time,
            self.num_frames,
            fps,
            (fps / self.orig_fps) * 100
        )

    def show_fps(self):
        self.setWindowTitle(self.get_fps())
