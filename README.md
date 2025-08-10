# 2bars

Cinematic Overlay for Clutches in CS2. A simple Python app that adds cinematic black bars at the top and bottom of your screen — perfect for adding that classic letterbox effect to videos, games, or presentations.

---

## Features

- Smooth animated black bars that slide in/out with easing
- Clean transparent overlay
- Global hotkey (`Ctrl + Alt + C`) to toggle bars on and off
- Lightweight and minimal dependencies

---

## Screenshots
With Overlay             |  Without Overlay
:-------------------------:|:-------------------------:
![](ss/1.png)  |  ![](ss/0.png)

## Requirements

- Python 3.6+
- PyQt5
- keyboard (for global hotkey support)

---

## Installation

1. Clone or download this repo.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

```python

python cinematic_bars.py
```

Press Ctrl + Alt + C to toggle the cinematic bars overlay on or off.

---

## Notes

- The app uses global keyboard hooks — running it may require admin or elevated privileges on some platforms.

- Only tested on Windows and Linux; macOS support may vary.
