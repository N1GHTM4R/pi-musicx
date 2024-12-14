from time import *  # noqa: F403 #NOTE: This ignores the error on this line.
from soundplayer import play_sound
import tkinter as Tk

root = Tk.Tk()

root.geometry("400x400")
root.title("Sound Tester")

play_sound("200hztest.wav")










root.mainloop()