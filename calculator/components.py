from tkinter import *


class NumericButton:
    @classmethod
    def create_button(cls, props):
        return Button(props["root"], text=props["text"], command=props["command"]).grid(row=props["row"], column=props["column"])


