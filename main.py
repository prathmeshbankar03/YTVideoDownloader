from pytube import YouTube
import requests
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
app = QtWidgets.QApplication([])
window = uic.loadUi("gui.ui")




def thumbnail_n_title():
    url=window.lineEdit.text()
    try:
        video=YouTube(url)
        thumbn=video.thumbnail_url
        window.label_4.setText(video.title)
        image=QImage()
        image.loadFromData(requests.get(thumbn).content)
        image_label=window.label_3
        image_label.setPixmap(QPixmap(image))
        window.label_5.setText("")
    except:
        window.label_5.setStyleSheet("QLabel#label_5"+"{"+"color:red;}")
        window.label_5.setText("Please Enter A Valid URL")

        return None
    
window.pushButton.clicked.connect(thumbnail_n_title)


def download():
    url=window.lineEdit.text()
    video=YouTube(url)
    video=video.streams.get_highest_resolution()
    video.download("Downloads")

window.pushButton_2.clicked.connect(download)


window.show()
app.exec()