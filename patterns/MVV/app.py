import tkinter as tk
import logging

from pattern import Model, Controller, View

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)

    logging.info('App is starting...')

    m = Model()
    v = View()

    c = Controller(m, v)

    v.init_window()

    v.bind(v.del_button, c.delete_item)
    v.bind(v.inputbox, c.add_item)

    c.init_view()
    v.run()