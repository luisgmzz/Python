import tkinter as tk
from calculator import get_equation, calculate


class App:
    def __init__(self):
        self.size = "400x400"

        self.root = tk.Tk()
        self.root.geometry(self.size)
        self.root.title("Equations")

        self.result = tk.StringVar()
        self.output = tk.Label(self.root, textvariable=self.result).pack()

        self.inp = tk.Entry(self.root, width=40)
        self.inp.place(x=100, y=200)
        self.button = tk.Button(
            self.root, text="Resolver", command=self.solucionar).pack()

        self.root.mainloop()

    def solucionar(self):
        a = self.inp.get()
        self.result.set(f"x={calculate(get_equation(a))}")


app = App()
