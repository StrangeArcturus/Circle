# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

from random import randint
import sys


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        print('[Qt] inited window')
        uic.loadUi('UI.ui', self)
        #self.pushButton.clicked.connect(self._click)
        self.pushButton.clicked.connect(self.paintEvent)
    
    def paintEvent(self, event=None) -> None:
        print('[Qt] paint event')
        qp: QPainter = QPainter()
        qp.begin(self)
        self.draw_circes(qp)
        qp.end()  
    
    def _click(self) -> None:
        print('[Qt] clicked button')
        qp: QPainter = QPainter()
        qp.begin(self)
        self.draw_circes(qp)
        qp.end()
    
    def draw_circes(self, qp: QPainter) -> None:
        print('[Qt] drawing random circles')
        qp.setBrush(QColor(255, 255, 0))
        for i in range(randint(2, 14)):
            radius: int = randint(0, 200)
            qp.drawEllipse(
                randint(0, 600),
                randint(0, 450),
                radius,
                radius
            )


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: Window = Window()
    window.show()
    sys.exit(app.exec())
