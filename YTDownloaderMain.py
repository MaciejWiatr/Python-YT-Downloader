from __future__ import unicode_literals
import youtube_dl
import os
from UiCos import *
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.test)

    def my_hook(self,d):
        if d['status'] == 'finished':
            self.ui.lineEdit.setText("Pobrane!")

    def test(self):
        link = self.ui.lineEdit.text()

        directory = QFileDialog.getExistingDirectory(self, "Choose your save directory", "/", QFileDialog.ShowDirsOnly)
        self.ui.lineEdit.setText("Trwa pobieranie...")
        try:
            os.chdir(directory)
        except:
            self.ui.lineEdit.setText("Wybrana lokalizacja nie istnieje!")
        ydl_opts = {
            'format': 'bestvideo',
            'progress_hooks': [self.my_hook]
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['{}'.format(link)])
        except:
            if link == '' or None:
                self.ui.lineEdit.setText("Wprowadź Link!")
            else:
                self.ui.lineEdit.setText("Coś poszło nie tak, spróbuj ponownie!")



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
