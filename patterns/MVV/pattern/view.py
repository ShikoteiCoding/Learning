import tkinter as tk
import logging

from typing import Callable, Any

def clicked():
    print("clicked")

class View:
    def __init__(self):
        ...

    def init_window(self):
        logging.info('Initializing window...')
        self.window = tk.Tk()

        # Configure design here
        self.window.configure(width=500, height=300, bg='lightgray')

        # Add components
        self.del_button = tk.Button(self.window, text ='Delete Item')
        self.del_button.place(x=400, y=200)
        
        self.listbox = tk.Listbox(self.window)
        self.listbox.place(x=10, y=10)

        self.textbox = tk.Text(self.window)
        self.textbox.place(x=10, y=200, height=20, width=300)

    @staticmethod
    def bind(component: tk.Tk, cmd: Callable):
        component.command = cmd

    def run(self):
        self.window.mainloop()