from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from desktop_bg import BgManager
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.bgm = BgManager()

        self.switchbtn = QPushButton('Get new image')
        self.switchbtn.clicked.connect(self.show_image_preview)

        self.confirmbtn = QPushButton('choose as bg')
        self.confirmbtn.clicked.connect(self.make_selection)

        self.photo = QLabel(self)
        self.photo.setPixmap(QPixmap(fr'{self.bgm.get_path()}\randomimg.jpg').scaled(600, 300))

        self.warning = QLabel('Be careful, you might never find the previous image again', self)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.photo)
        self.main_layout.addWidget(self.switchbtn)
        self.main_layout.addWidget(self.warning)
        self.main_layout.addWidget(self.confirmbtn)

    
    def show_image_preview(self):
        self.bgm.make_request()
        self.photo.setPixmap(QPixmap(fr'{self.bgm.get_path()}\randomimg.jpg').scaled(600, 300))

    
    def make_selection(self):
        self.bgm.set_desktop_bg()

    
if __name__ == '__main__':
    app = QApplication([])
    widget = App()
    widget.setWindowTitle('random bg generator')
    widget.resize(600, 300)
    widget.show()

    sys.exit(app.exec())