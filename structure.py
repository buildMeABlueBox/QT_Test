from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()
        label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)
        button.clicked.connect(self.close)

app = QApplication(sys.argv) #Only should have one instance of QApplication
dialog = HelloWorld() #QDialog is a Window
dialog.show()
app.exec_()

