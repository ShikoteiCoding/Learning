import tkinter as tk
import logging

def clicked():
    print("clicked")

class View:
    def __init__(self):
        ...

    def init_window(self):
        logging.info("Initializing window...")
        self.window = tk.Tk()

        # Configure design here
        self.window.configure(width=500, height=300, bg='lightgray')

        # Add components
        self.del_button = tk.Button(self.window, text ="Delete Item", command=clicked)
        self.del_button.place(x=400, y=200)
        
        self.listbox = tk.Listbox(self.window)
        self.listbox.place(x=10, y=10)

        self.textbox = tk.Text(self.window, height=20, width=400)
        self.textbox.place(x=10, y=200)

    def run(self):
        self.window.mainloop()