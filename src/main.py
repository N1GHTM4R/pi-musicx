from time import *  # noqa: F403 #NOTE: This ignores the error on this line.
from soundplayer import play_sound
import tkinter as Tk

root = Tk.Tk()

root.geometry("400x400")
root.title("Sound Tester")





def button_clicked():
    play_sound("200hztest.wav")
    

# Creating a button with specified options
button = Tk.Button(root, 
                   text="test audio", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)






root.mainloop()