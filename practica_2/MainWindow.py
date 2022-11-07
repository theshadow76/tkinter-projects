import sys
from PyQt6.QtGui import QIcon
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6
import PyQt6.QtCore
from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QMessageBox
from tkinter import messagebox as msgbox
import webbrowser
import time

from pyparsing import Keyword


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    Accept = QPushButton(widget)
    Accept.setText("Accept")
    Accept.move(300, 300)
    Accept.show()
    
    if (Accept.clicked == True):
        Accept.clicked.connect(AcceptLogic)
        try:
            Accept.clicked = True
        except:
            time.sleep(3)
            print("ahora si, Error")
    else:
        try:
            time.sleep(3)
            print("ahora si, Error")
        except:
            Accept.clicked = True

    widget.setGeometry(50, 50, 700, 700)

    widget.setWindowTitle("window")
    widget.show()

    sys.exit(app.exec())

def AcceptLogic():
    import selenium
    from selenium import webdriver

    showmsg1 = msgbox.YESNO

    if (showmsg1 == True):
        try:
            test2 = webbrowser.open("https://theshadowtech.com/")
        except:
            msgbox.showwarning()
        while (test2 == True):
            driver = webdriver.Chrome('/Users/vigowalker/Documents/chromedriver')
            driver.get("https://theshadowtech.com/")
            try:
                ck = driver.get_cookies()
                ck.replace = "<script>alert('uff')</script>"
            except:
                driver.close()
            break
    else:
        test1 = msgbox.Message()
        test1.text = "AH"
    

if __name__ == "__main__":
    window()