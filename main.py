from classes import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def win():
    print("Win placeholder")


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.first = 1  # starting room
        self.doors = [Door("Cupboard door", {1: 0, 0: 1})]

        self.places = [
            Thing(
                "Walk-in cupboard",
                items=[Thing("Pile of clothes", items=[Thing("Afikoman", action=win)])],
                places=[self.doors[0]],
            ),
            Thing("Master bedroom", places=[self.doors[0]]),
        ]

    def run(self):
        self.name = tk.StringVar(self, self.places[self.first].name)
        self.desc = tk.StringVar(self, self.places[self.first].desc)

        self.name_label = ttk.Label(self, textvariable=self.name)
        self.desc_label = ttk.Label(self, textvariable=self.desc)

        self.name_label.grid(column=0, row=0, padx=7, pady=7)
        self.mainloop()


if __name__ == "__main__":
    game = Game()
    game.run()
