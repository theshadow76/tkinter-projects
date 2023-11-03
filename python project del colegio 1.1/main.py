import PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt

def holaAct():
    print("holaAct")

def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 200)
    w.move(300, 300)
    w.setStyleSheet("background-color: gold")

    w.setWindowTitle('ShadowTest')

    hola = QLabel(w)
    hola.setText("ShadowTest")
    hola.setStyleSheet("color: green")
    hola.move(0, 0)
    hola.show()

    btn1 = QPushButton(w)
    btn1.setStyleSheet("background-color: green")
    btn1.setText("press me")
    btn1.move(5, 15)
    btn1.show()

    btn1.clicked.connect(holaAct)
    
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()