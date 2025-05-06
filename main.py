import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl

from main_screen import *



class Main_screen(QMainWindow):
    def __init__ (self):   
        super().__init__ ()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # init button events 
        self.ui.onBtn_lamp.clicked.connect(self.lamp_on)
        self.ui.offBtn_lamp.clicked.connect(self.lamp_off)
        self.ui.onBtn_fan.clicked.connect(self.fan_on)
        self.ui.offBtn_fan.clicked.connect(self.fan_off)
        self.ui.onBtn_speaker.clicked.connect(self.speaker_on)
        self.ui.offBtn_speaker.clicked.connect(self.speaker_off)
        self.ui.onBtn_tv.clicked.connect(self.tv_on)
        self.ui.offBtn_tv.clicked.connect(self.tv_off)
        self.ui.closeBtn.clicked.connect(self.close)

        # Initialize sound effect
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile(resource_path("resource/sound/hustlanga_all_day.wav")))
        self.sound.setVolume(0.5)  # Volume level (0.0 to 1.0)

    def lamp_on(self):
        self.ui.lamp.setPixmap(QtGui.QPixmap(resource_path("resource/images/lamp_on.png")))
    def lamp_off(self):
        self.ui.lamp.setPixmap(QtGui.QPixmap(resource_path("resource/images/lamp_off.png")))

    def fan_on(self):
        self.ui.fan.setPixmap(QtGui.QPixmap(resource_path("resource/images/fan_on.png")))
    def fan_off(self):
        self.ui.fan.setPixmap(QtGui.QPixmap(resource_path("resource/images/fan_off.png")))

    def speaker_on(self):
        self.ui.speaker.setPixmap(QtGui.QPixmap(resource_path("resource/images/speaker_on.png")))
        self.sound.play()  
    def speaker_off(self):
        self.ui.speaker.setPixmap(QtGui.QPixmap(resource_path("resource/images/speaker_off.png")))
        self.sound.stop()

    def tv_on(self):
        self.ui.tv.setPixmap(QtGui.QPixmap(resource_path("resource/images/TV_on.png")))
    def tv_off(self):
        self.ui.tv.setPixmap(QtGui.QPixmap(resource_path("resource/images/TV_off.png")))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main_screen()
    ui.show()
    sys.exit(app.exec())