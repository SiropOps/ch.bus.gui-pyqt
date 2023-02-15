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
            lambda: self.wifiBtn_clicked(wifiBtn))

        layout.addWidget(wifiBtn, 0, 0)

        vpnBtn = QPushButton(
            icon=QIcon("./icons/network-cloud.png"),
            text="VPN UP/DOWN",
            parent=self
        )

        vpnBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        vpnBtn.clicked.connect(self.action.vpn)

        layout.addWidget(vpnBtn, 0, 1)

        shutdownBtn = QPushButton(
            icon=QIcon("./icons/control-power.png"),
            text="ShutDown",
            parent=self
        )

        shutdownBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        shutdownBtn.clicked.connect(self.action.shutdown)

        layout.addWidget(shutdownBtn, 1, 0)

        overBtn = QPushButton(
            icon=QIcon("./icons/thumb.png"),
            text="La Fête est Finie!",
            parent=self
        )

        overBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        overBtn.clicked.connect(self.action.over)
        layout.addWidget(overBtn, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def wifiBtn_clicked(self, button):
        if self.action.wifi(button.isChecked()) is False:
            button.setStyleSheet("background-color: red")
        elif button.isChecked() is True:
            button.setStyleSheet("background-color: green")
        elif button.isChecked() is False:
            button.setStyleSheet("background-color: yellow")


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
