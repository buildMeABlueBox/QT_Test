from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class HelloWorld(QDialog): #QDialog is a Window
    def __init__(self):
        QDialog.__init__(self)
        layout = QGridLayout()
        label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)
        button.clicked.connect(self.close)

app = QApplication(sys.argv) #Only should have one instance of QApplication
dialog = HelloWorld()
dialog.show()
app.exec_()

