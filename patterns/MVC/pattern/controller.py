import logging

import tkinter as tk

from pattern.model import Model
from pattern.view import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

        self.view.bind(self.view.del_button, "<Button>", self.handle_delete)
        self.view.bind(self.view.inputbox, "<Return>", self.handle_input)

        self.update_task_list()

    # Handlers
    def handle_delete(self, event: tk.Event) -> None:
        el = self.view.get_active_task()
        logging.info(f"{str(event)}. Delete input is on {el or None}")

        if not el:
            return

        self.model.delete_item(el[0])
        self.update_task_list()

    def handle_input(self, event: tk.Event) -> None:
        input = self.view.get_entry_text()
        logging.info(f'{str(event)}. Text input is "{input or None}"')

        if not input:
            return

        self.model.add_item(input)
        self.view.clear_entry_text()
        self.update_task_list()

    def update_task_list(self):
        # Less coupled version: controller is responsible to update view (can be the model though)
        items = self.model.get_items()
        self.view.clear_task_list()

        if not items:
            return

        for item in items:
            self.view.add_task_to_list(item)

    def run(self):
        self.view.mainloop()
