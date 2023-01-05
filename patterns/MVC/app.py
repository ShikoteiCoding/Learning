import tkinter as tk
import logging

from pattern import Model, Controller, View


def main() -> None:
    logging.info("App is starting...")

    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.run()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    main()
