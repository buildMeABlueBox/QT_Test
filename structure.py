from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv) #Only should have one instance of QApplication
dialog = QDialog() #QDialog is a Window
dialog.show()
app.exec_()

