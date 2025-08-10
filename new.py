import sys
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor

class BlackBars(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate)
        self.animation_timer.start(16)  # ~60 FPS

        self.progress = 0.0
        self.target_progress = 0.0
        self.speed = 0.15  # fast transition
        self.bar_height_ratio = 0.12
        self.hide()

    def animate(self):
        # Smooth easing towards target progress
        if abs(self.progress - self.target_progress) > 0.01:
            self.progress += (self.target_progress - self.progress) * self.speed
            self.update()
        else:
            self.progress = self.target_progress
            if self.progress == 0:
                self.hide()
            self.update()

    def toggle(self):
        if self.target_progress == 0:
            self.show()
            self.target_progress = 1.0
        else:
            self.target_progress = 0.0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(0, 0, 0))
        painter.setPen(Qt.NoPen)

        # Slide bars in proportion to progress
        max_height = int(self.height() * self.bar_height_ratio)
        current_height = int(max_height * self.progress)

        painter.drawRect(0, 0, self.width(), current_height)
        painter.drawRect(0, self.height() - current_height, self.width(), current_height)

app = QApplication(sys.argv)
bars = BlackBars()
keyboard.add_hotkey("ctrl+alt+c", bars.toggle)
sys.exit(app.exec_())
