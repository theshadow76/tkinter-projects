import sys
import os
from PyQt6.QtGui import QIcon
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6
import PyQt6.QtCore
from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QFileDialog

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    btnTest = QPushButton(widget)
    btnTest.setText("Test")
    btnTest.move(50, 50)
    btnTest.clicked.connect(btnTestPress)

    widget.setGeometry(50, 50, 320, 200)

    widget.setWindowTitle("Shadow Example")
    widget.show()

    sys.exit(app.exec())

def btnTestPress(window):
    file_filtre = 'Text Files (*.txt)'
    response = QFileDialog.getOpenFileName(
        parent = window,
        caption = 'Select a text file',
        director = os.getcwd(),
        filter = file_filtre,
        initialFilter = 'Text Files (*.txt)'
    )
    return response

if __name__ == '__main__':
    window()