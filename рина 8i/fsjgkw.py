import os
from PyQt6.QWidgets import (
    QApplication, QWidget,
    QFileDialog, # dialog otkrytia failov (i papok)
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

from PyQt5.QtCore import Qt # nuzhna konstanta Qt.KeepAspectRatio dlya izmenenya razmerov s sohraneniyem proporcyi
from PyQt5.QtGui import QPixmap # optimizirovannaya dlya pokaza na ekrane kartinka

from PIL import Image
from PIL.ImageQt import ImageQt
from PIL import ImageFilter
from PIL.ImageFilter import SHARPEN

app = QApplication([])
win = QWidget()