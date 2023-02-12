import os

from PyQt5.QtGui import QColor, QIcon, QPalette
from PyQt5.QtWidgets import (QGridLayout, QMainWindow, QPushButton,
                             QSizePolicy, QStyle, QWidget)

from actions.action import Action


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.action = Action()

        self.setWindowTitle("BUS-GUI")

        layout = QGridLayout()

        wifiBtn = QPushButton(
            icon=QIcon("./icons/wi-fi.png"),
            text="Wifi UP/DOWN",
            parent=self
        )

        wifiBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        wifiBtn.setCheckable(True)
        wifiBtn.clicked.connect(
            lambda: self.the_button_was_clicked(wifiBtn))

        layout.addWidget(wifiBtn, 0, 0)

        button = QPushButton("Press Me! 2")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setCheckable(True)
        layout.addWidget(button, 0, 1)

        button = QPushButton("Press Me! 3")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(button, 1, 0)

        button = QPushButton("Press Me! 4")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(button, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self, button):
        if self.action.the_button_was_clicked() is False:
            button.setStyleSheet("background-color: red")
            # button.setAutoFillBackground(True)

            # palette = button.palette()
            # palette.setColor(QPalette.Window, QColor('red'))
            # button.setPalette(palette)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
