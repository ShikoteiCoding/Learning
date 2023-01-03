from pattern.model import Model
from pattern.view import View

class Controller:

    def __init__(self, model:Model, view:View):
        self.model = model
        self.view = view

    def init_view(self):
        self.update_view()

    def get_items(self):
        self.model.get_items()
        self.update_view()

    def delete_item(self, name):
        self.model.delete_item(name)
        self.update_view()

    def add_item(self):
        self.update_view()

    def update_view(self):
        # Less coupled version: controller is responsible to update view (can be the model though)
        
        for item in self.model.items:
            self.view.insert(0, item)