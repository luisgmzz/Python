from tkinter import *
from time import sleep


class App:
    def __init__(self):
        self.time = 0
        self.clicks = 0
        self.size = "400x400"

        self.wn = Tk()
        self.wn.geometry(self.size)

        self.textTime = StringVar()
        self.textTime.set(self.time)
        self.labelTime = Label(self.wn, textvariable=self.textTime).pack()

        self.textClicks = StringVar()
        self.textClicks.set(self.clicks)
        self.labelClicks = Label(self.wn, textvariable=self.textClicks).pack()

        self.button = Button(self.wn, text="Click",
                             command=self.changeText).pack()

        self.wn.mainloop()

        for i in range(10):
            self.time = i
            sleep(1)
            self.textTime.set(self.time)

    def changeText(self):
        self.clicks += 1
        self.textClicks.set(self.clicks)


app = App()
