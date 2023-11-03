import sys
from PyQt6.QtGui import QIcon
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6
import PyQt6.QtCore
from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QFrame
from PyQt6.QtCore import QColor

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    canvas = QFrame
    canvas.size(30, 50)
    canvas.backgroundColor = QColor(21, 21, 21)
    canvas.show()


    widget.setGeometry(50, 50, 320, 200)

    widget.setWindowTitle("Shadow Manager")
    widget.show()

    sys.exit(app.exec_())
if __name__ == '__main__':
    window()