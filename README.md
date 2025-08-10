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
Without Overlay             |  With Overlay
:-------------------------:|:-------------------------:
![](https://cdn.discordapp.com/attachments/926176591736889385/1404140183342944318/kiBOEPE.png?ex=689a1af3&is=6898c973&hm=aae0d09874da86d292f6bf9e0854e0a2ace0aa1bd7734c640fcb8c8354f4a750&)  |  ![](https://cdn.discordapp.com/attachments/926176591736889385/1404140269783224401/1Xpo43R.png?ex=689a1b07&is=6898c987&hm=e12323761958838c265114396692de9792250cc1b3c05505159330217cfd7386&)

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
