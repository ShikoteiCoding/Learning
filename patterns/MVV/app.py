import tkinter as tk
import logging

from pattern import Model, Controller, View

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)

    logging.info("App is starting...")

    m = Model()
    c = Controller()

    v = View()
    v.init_window()
    v.run()

