import tkinter as tk
from tkinter import messagebox

#https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter

root = tk.Tk()

tk.messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()