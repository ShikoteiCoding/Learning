import logging

import tkinter as tk

from pattern.model import Model
from pattern.view import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def init_view(self):

        self.view.bind(self.view.del_button, "<Button>", self.handle_delete)
        self.view.bind(self.view.inputbox, "<Return>", self.handle_input)

        self.update_view()

    # Model management
    def get_items(self):
        self.model.get_items()
        self.update_view()

    def delete_item(self, name):
        self.model.delete_item(name)
        self.update_view()

    def add_item(self):
        self.update_view()

    # Handlers
    def handle_delete(self, event: str) -> int:
        el = self.view.listbox.get(tk.ACTIVE)
        logging.info(f"{event}. Delete input is on {el or None}")

        if not el:
            return 0

        self.model.delete_item(el[0])
        self.update_view()

        return 1

    def handle_input(self, event: str) -> int:
        input = self.view.inputbox.get(1.0, "end-1c").strip()
        logging.info(f'{event}. Text input is "{input or None}"')

        if not input:
            return 0

        self.model.add_item(input)
        self.view.inputbox.delete(1.0, tk.END)
        self.update_view()

        return 1

    def update_view(self):
        # Less coupled version: controller is responsible to update view (can be the model though)
        items = self.model.get_items()
        self.view.listbox.delete(0, tk.END)

        if not items:
            return

        for item in items:
            self.view.listbox.insert(tk.END, item)
