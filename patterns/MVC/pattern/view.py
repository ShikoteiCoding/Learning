import tkinter as tk
import logging

from typing import Callable, Any


def clicked():
    print("clicked")


class View:
    def __init__(self):

        self.create_ui()

    def create_ui(self):
        logging.info("Initializing window...")
        self.window = tk.Tk()

        # Configure design here
        self.window.configure(width=500, height=300, bg="lightgray")

        # Add components
        self.del_button = tk.Button(self.window, text="Delete Item")
        self.del_button.place(x=400, y=200)

        self.listbox = tk.Listbox(self.window)
        self.listbox.place(x=10, y=10)

        self.inputbox = tk.Text(self.window)
        self.inputbox.place(x=10, y=200, height=20, width=300)

    @staticmethod
    def bind(
        component: tk.Tk, event_type: str, callback: Callable[[tk.Event], None]
    ) -> None:
        component.bind(event_type, callback)

    def clear_entry_text(self) -> None:
        self.inputbox.delete(1.0, tk.END)

    def get_entry_text(self) -> str:
        return self.inputbox.get(1.0, tk.END).strip()

    def clear_task_list(self) -> None:
        self.listbox.delete(0, tk.END)

    def add_task_to_list(self, item: str) -> None:
        self.listbox.insert(tk.END, item)

    def get_active_task(self) -> tuple:
        return self.listbox.get(self.listbox.curselection())

    def mainloop(self):
        self.window.mainloop()
