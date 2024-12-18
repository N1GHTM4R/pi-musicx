from time import *  # noqa: F403 #NOTE: This ignores the error on this line.
from soundplayer import play_sound, loopsound, stop_loopsound
import tkinter as Tk

root = Tk.Tk()

root.geometry("400x400")
root.title("Sound Tester")





def single_button_clicked():
    print("single clicked:)")
    play_sound("200hztest.wav")
    
def loop_button_clicked():
    loopsound("200hztest.wav")

def stop_button_clicked():
    stop_loopsound()
# Creating a button with specified options
singlebutton = Tk.Button(root, 
                   text="test audio", 
                   command=single_button_clicked,
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

singlebutton.pack(padx=20, pady=20)

# Creating a button to start looping the sound
loopbutton = Tk.Button(root, 
                   text="Start Looping Audio", 
                   command=loop_button_clicked,
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

loopbutton.pack(padx=20, pady=20)

# Creating a button to stop looping the sound
stop_button = Tk.Button(root, 
                        text="Stop Looping Audio", 
                        command=stop_button_clicked,
                        activebackground="red", 
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

stop_button.pack(padx=20, pady=20)





root.mainloop()