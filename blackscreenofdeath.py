import tkinter as tk
import keyboard
import time
import threading

# Easing function: cubic ease in-out
def ease_in_out_cubic(t):
    if t < 0.5:
        return 4 * t * t * t
    else:
        return 1 - pow(-2 * t + 2, 3) / 2

class CinematicOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.config(bg="black")
        self.root.overrideredirect(True)

        self.screen_w = self.root.winfo_screenwidth()
        self.screen_h = self.root.winfo_screenheight()

        self.bar_height = 0
        self.target_height = int(self.screen_h * 0.12)  # 12% screen height bars
        self.animation_duration = 0.5  # seconds
        self.animation_steps = 60

        self.top_bar = tk.Frame(self.root, bg="black", height=0, width=self.screen_w)
        self.bottom_bar = tk.Frame(self.root, bg="black", height=0, width=self.screen_w)

        self.top_bar.place(x=0, y=0)
        self.bottom_bar.place(x=0, y=self.screen_h)

        self.visible = False
        threading.Thread(target=self.listen_hotkey, daemon=True).start()
        self.root.mainloop()

    def listen_hotkey(self):
        keyboard.add_hotkey("ctrl+alt+c", self.toggle)
        keyboard.wait()  # keep thread alive

    def toggle(self):
        threading.Thread(target=self.animate_bars, daemon=True).start()

    def animate_bars(self):
        start_height = self.bar_height
        end_height = self.target_height if not self.visible else 0
        self.visible = not self.visible

        for i in range(self.animation_steps + 1):
            t = i / self.animation_steps
            eased_t = ease_in_out_cubic(t)
            new_height = int(start_height + (end_height - start_height) * eased_t)
            self.update_bars(new_height)
            time.sleep(self.animation_duration / self.animation_steps)

        self.bar_height = end_height

    def update_bars(self, height):
        self.top_bar.config(height=height)
        self.bottom_bar.config(height=height)
        self.bottom_bar.place(x=0, y=self.screen_h - height)
        self.root.update_idletasks()

if __name__ == "__main__":
    CinematicOverlay()
