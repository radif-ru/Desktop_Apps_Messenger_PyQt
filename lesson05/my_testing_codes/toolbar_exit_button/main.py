# ---------------- Графический интерфейс пользователя. PyQt5 ------------------
#                   Демонстрация создания событий (Action)

"""
ZetCode PyQt5 tutorial 

This program creates a toolbar. 
The toolbar has one action, which terminates the application, if triggered.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit/Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit tratata')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)

        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
