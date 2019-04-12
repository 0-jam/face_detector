import cv2
from PySide2 import QtGui, QtWidgets


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

        self.scene = QtWidgets.QGraphicsScene()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

    def setCVImage(self, cvimage):
        self.scene.addItem(QtWidgets.QGraphicsPixmapItem(cv2pixmap(cvimage)))
        self.view.setScene(self.scene)
