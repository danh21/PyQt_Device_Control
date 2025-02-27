import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl



class Main_screen(QMainWindow):
    def __init__ (self):   
        super().__init__ ()     # Call parent class (QMainWindow) constructor
        loadUi ("main_screen.ui",self)

        # init button events 
        self.onBtn_lamp.clicked.connect(self.lamp_on)
        self.offBtn_lamp.clicked.connect(self.lamp_off)
        self.onBtn_fan.clicked.connect(self.fan_on)
        self.offBtn_fan.clicked.connect(self.fan_off)
        self.onBtn_speaker.clicked.connect(self.speaker_on)
        self.offBtn_speaker.clicked.connect(self.speaker_off)
        self.onBtn_tv.clicked.connect(self.tv_on)
        self.offBtn_tv.clicked.connect(self.tv_off)
        self.closeBtn.clicked.connect(self.close)

        # Initialize sound effect
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("resource/sound/hustlanga_all_day.wav"))
        self.sound.setVolume(0.5)  # Volume level (0.0 to 1.0)

    def lamp_on(self):
        self.lamp.setPixmap(QtGui.QPixmap("resource/images/lamp_on.png"))
    def lamp_off(self):
        self.lamp.setPixmap(QtGui.QPixmap("resource/images/lamp_off.png"))

    def fan_on(self):
        self.fan.setPixmap(QtGui.QPixmap("resource/images/fan_on.png"))
    def fan_off(self):
        self.fan.setPixmap(QtGui.QPixmap("resource/images/fan_off.png"))

    def speaker_on(self):
        self.speaker.setPixmap(QtGui.QPixmap("resource/images/speaker_on.png"))
        self.sound.play()  
    def speaker_off(self):
        self.speaker.setPixmap(QtGui.QPixmap("resource/images/speaker_off.png"))
        self.sound.stop()

    def tv_on(self):
        self.tv.setPixmap(QtGui.QPixmap("resource/images/TV_on.png"))
    def tv_off(self):
        self.tv.setPixmap(QtGui.QPixmap("resource/images/TV_off.png"))



if __name__ == '__main__':
    app = QApplication (sys.argv) #init app
    main = Main_screen()
    main.show()
    sys.exit(app.exec())