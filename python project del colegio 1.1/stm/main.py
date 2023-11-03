import PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt

def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1920, 1080)
    w.move(300, 300)
    w.setStyleSheet("background-color: #EEEEEE")

    w.setWindowTitle('ShadowTest')

    pn1 = QFrame(w)
    pn1.move(10, 9)
    pn1.show()
    pn1.setStyleSheet("background-color: black; width: 100%; height: 7%")
    
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()