from pattern.model import Model
from pattern.view import View

class Controller:

    def __init__(self, model:Model, view:View):
        self.model = model
        self.view = view

    def get_items(self):
        return self.model.get_items()

    def delete_item(self, name):
        return self.model.delete_item(name)

    def add_item(self):
        ...

    def update_view(self):
        # Less coupled version: controller is responsible to update view (can be the model though)
        ...