import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt line Edit"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('rubble_paw_patrol_canine_patrol_icon_263827.ico'))

        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(260, 30)
        self.textbox.setText("Set this text value")
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())