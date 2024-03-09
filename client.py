import asyncio, os, sys, threading
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtGui import QIcon

from GUI.window import WindowSetter # Includes Constants
from back.server import Server

os.environ["XDG_SESSION_TYPE"] = "xcb"


class MainWindow(WindowSetter):
    def __init__(self):
        super().__init__()
        self.stop_flag = False
        self.server = Server()
        self.loop = None
        self.thread = None


    def play_clicked(self):
        """Event for PLAY button clicked."""
        self.play_button.hide()
        self.stop_flag = False
        self.run_event_loop()

    def stop_clicked(self):
        """Event for PLAY button clicked."""
        self.play_button.show()
        self.stop_flag = True

    def run_event_loop(self):
        """Starts the asyncio event loop in a separate thread."""
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self.loop.run_until_complete, args=(self.poll_endpoint(),))
        self.thread.start()

    async def poll_endpoint(self):
        """Send requests to the endpoint periodically."""
        while not self.stop_flag:
            response = await asyncio.to_thread(self.server.send_call)
            print(response)
            await asyncio.sleep(10)
    def mousePressEvent(self, event):
        """Set the possibility of capturing the window by mouse clicking as true."""
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        """Set the possibility of moving the window by mouse as true."""
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def enterEvent(self, event):
        """Shows close button when mouse is in the window."""
        if not self.close_button:
            self.close_button = QPushButton('', self)
            close_icon = QIcon('src/icons/close_icon.png')  # Path to the close button icon
            self.close_button.setIcon(close_icon)
            self.close_button.setIconSize(QSize(self.ICON_X_WIDTH, self.ICON_X_HEIGHT))
            self.close_button.setGeometry(self.ICON_X_X, self.ICON_X_Y, self.ICON_X_WIDTH, self.ICON_X_HEIGHT)
            self.close_button.setStyleSheet("border: none")
            self.close_button.clicked.connect(self.close)  # By pressing close button, the window closes
            self.close_button.show()

    def leaveEvent(self, event):
        """Hides close button when mouse is out of the window."""
        if self.close_button:
            self.close_button.deleteLater()
            self.close_button = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
