import sys
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor
import argparse

class BlackBars(QWidget):
    def __init__(self, bar_height_ratio=0.12, speed=0.15):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate)
        self.animation_timer.start(16)  # ~60 FPS

        self.progress = 0.0
        self.target_progress = 0.0
        self.speed = speed
        self.bar_height_ratio = bar_height_ratio
        self.hide()

    def animate(self):
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

        max_height = int(self.height() * self.bar_height_ratio)
        current_height = int(max_height * self.progress)

        painter.drawRect(0, 0, self.width(), current_height)
        painter.drawRect(0, self.height() - current_height, self.width(), current_height)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Black Bars Application")
    parser.add_argument("--bar-height-ratio", type=float, default=0.12, help="Height ratio of the bars")
    parser.add_argument("--speed", type=float, default=0.15, help="Transition speed")
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    app = QApplication(sys.argv)
    bars = BlackBars(bar_height_ratio=args.bar_height_ratio, speed=args.speed)
    
    try:
        keyboard.add_hotkey("ctrl+alt+c", bars.toggle)
        print("KEEP THIS WINDOW ALIVE.")
        print("Use Ctrl+Alt+C to Toggle")
    except Exception as e:
        print(f"Failed to bind hotkey: {e}")
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
