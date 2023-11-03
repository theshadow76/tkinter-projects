import os
import sys
from PyQt6.QtGui import QIcon
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6
import PyQt6.QtCore
from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QApplication, QMenuBar, QPushButton, QFileDialog, QVBoxLayout

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.btnTest = QPushButton()
        self.btnTest.move(50, 50)
        # self.btnTest.clicked.connect(self.btnTestPress())
        layout.addWidget(self.btnTest)

    def btnTestPress(self):
        file_filstrer = "Text Files (*.txt)"
        resposne = QFileDialog.getOpenFileName(
            parent=self,
            caption='select a Text File',
            directory=os.getcwd(),
            filter=file_filstrer,
            initialFilter='Text Files (*.txt)'
        )
        return resposne

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = main()
    myapp.show()

    try:
        sys.exit(myapp.exec())
    except:
        print("window closing...")
