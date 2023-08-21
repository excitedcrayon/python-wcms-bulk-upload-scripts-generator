#!/usr/bin/python3

from tkinter import Tk
from configuration import config

class WCMSGenerator(Tk):
    def __init__(self):
        super().__init__()

        self.window_dimension_width = config.SCREEN_WIDTH
        self.window_dimension_height = config.SCREEN_HEIGHT

if __name__ == "__main__":
    WCMSGenerator()