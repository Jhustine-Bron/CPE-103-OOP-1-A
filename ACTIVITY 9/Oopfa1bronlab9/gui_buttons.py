import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt Button"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('rubble_paw_patrol_canine_patrol_icon_263827.ico'))

        self.button = QPushButton("Click me!", self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(110,95)

        self.button2 = QPushButton("Register", self)
        self.button2.setToolTip("This button does nothing yet...")
        self.button2.move(110, 145)

        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


