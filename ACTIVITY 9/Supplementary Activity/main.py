import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "Account Registration System"
        self.x = 200
        self.y = 200
        self.width = 350
        self.height = 350
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('chart_flowchart_document_write_file_note_pencil_draft_icon_262111.ico'))

        self.setStyleSheet("background-color: #CFFAAA;")

        self.textboxlbl = QLabel("Account Registration System ", self)
        self.textboxlbl.move(30, 5)
        self.textboxlbl.setFont(QFont("Consolas", 15, QFont.Bold ))

        self.textboxlbl1 = QLabel("First Name: ", self)
        self.textboxlbl1.move(15,45)
        self.textboxlbl1.setFont(QFont("Consolas", 11))

        self.textbox = QLineEdit(self)
        self.textbox.move(110, 35)
        self.textbox.resize(224, 35)
        self.textbox.setText("Juan ")
        self.textbox.setStyleSheet("background-color: #F1F2F1;")

        self.textboxlbl2 = QLabel("Last Name: ", self)
        self.textboxlbl2.move(15, 85)
        self.textboxlbl2.setFont(QFont("Consolas", 11))

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(110, 75)
        self.textbox1.resize(224, 35)
        self.textbox1.setText("Dela Cruz")
        self.textbox1.setStyleSheet("background-color: #F1F2F1;")

        self.textboxlbl3 = QLabel("Username: ", self)
        self.textboxlbl3.move(15, 125)
        self.textboxlbl3.setFont(QFont("Consolas", 11))

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(110, 115)
        self.textbox2.resize(224, 35)
        self.textbox2.setText("bronito_24")
        self.textbox2.setStyleSheet("background-color: #F1F2F1;")

        self.textboxlbl4 = QLabel("Password: ", self)
        self.textboxlbl4.move(15, 165)
        self.textboxlbl4.setFont(QFont("Consolas", 11))

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(110, 155)
        self.textbox3.resize(224, 35)
        self.textbox3.setText("Ilovehersomuch05")
        self.textbox3.setStyleSheet("background-color: #F1F2F1;")

        self.textboxlbl5 = QLabel("Email Address: ", self)
        self.textboxlbl5.move(5, 205)
        self.textboxlbl5.setFont(QFont("Consolas", 10))

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(110, 195)
        self.textbox4.resize(224, 35)
        self.textbox4.setText("bronjhustine24@gmail.com")
        self.textbox4.setStyleSheet("background-color: #F1F2F1;")

        self.textboxlbl6 = QLabel("Contact No.: ", self)
        self.textboxlbl6.move(5, 245)
        self.textboxlbl6.setFont(QFont("Consolas", 11))

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(110, 235)
        self.textbox5.resize(224, 35)
        self.textbox5.setText("09624116138")
        self.textbox5.setStyleSheet("background-color: #F1F2F1;")

        self.button = QPushButton("SUBMIT", self)
        self.button.setFont(QFont("Consolas", 11))
        self.button.setToolTip("why are you looking at this >:(")
        self.button.move(75, 285)
        self.button.resize(125, 50)
        self.button.setStyleSheet("background-color: #8FF185;")

        self.button1 = QPushButton("CLEAR", self)
        self.button1.setToolTip("STOP LOOKING!")
        self.button1.move(200, 285)
        self.button1.resize(125, 50)
        self.button1.setStyleSheet("background-color: #F18585;")


        self.show()
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())