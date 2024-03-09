import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QColor, QPalette, QFont, QIcon

from .const import Constants

class WindowSetter(Constants, QWidget):
    def __init__(self):
        super().__init__()

        # Setting BG color and border style
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(self.BG_COLOR_R, self.BG_COLOR_G, self.BG_COLOR_B))  # Бирюзовый фон
        self.setPalette(palette)
        self.setStyleSheet("border: 3px solid grey; border-radius: 20px")

        # Add main label
        self.background_label = QLabel(self)
        self.background_label.setGeometry(self.LABEL_X, self.LABEL_Y, self.LABEL_WIDTH, self.LABEL_HEIGHT)
        self.background_label.setStyleSheet(
            "background-color: rgb({}, {}, {}); "
            "border: 3px solid grey; border-radius: 20px;"
            .format(self.BG_COLOR_R, self.BG_COLOR_G, self.BG_COLOR_B)
        )

        # Add a label for words
        self.result_label = QLabel('Waiting for result...', self)
        self.result_label.setGeometry(
            self.WORDS_LABEL_X,
            self.WORDS_LABEL_Y,
            self.WORDS_LABEL_WIDTH,
            self.WORDS_LABEL_HEIGHT
        )
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.hide()

        # Create PLAY button
        self.play_button = QPushButton('PLAY', self)
        self.play_button.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.play_button.setGeometry(self.BUTTONS_X, self.PLAY_BUTTON_Y, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT)
        self.play_button.clicked.connect(self.play_clicked)
        self.play_button.move((self.WINDOW_WIDTH - self.BUTTONS_WIDTH) // 2, 50)

        # Create STOP button
        self.stop_button = QPushButton('STOP', self)
        self.stop_button.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.stop_button.setGeometry(self.BUTTONS_X, self.STOP_BUTTON_Y, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT)
        self.stop_button.clicked.connect(self.stop_clicked)
        self.stop_button.move((self.WINDOW_WIDTH - self.BUTTONS_WIDTH) // 2, 120)

        # Set window parameters
        self.setGeometry(self.WINDOW_X, self.WINDOW_Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        self.close_button = None  # Set close button invisible for a start
        self.oldPos = self.pos()  # Old window position

        # Hide top panel
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # Set the BG transparent
        self.setAttribute(Qt.WA_TranslucentBackground)