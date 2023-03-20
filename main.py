from classes import *
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox


def win():
    print("Win placeholder")


class Game(ctk.CTk):
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
        self.minsize(width=150, height=150)
        self.name = tk.StringVar(self, self.places[self.first].name)
        self.desc = tk.StringVar(self, self.places[self.first].desc)
        self.desc.set("bla bla bla")

        self.columnconfigure([0], weight=1)
        self.rowconfigure([0, 1], weight=1)

        self.name_label = ctk.CTkLabel(
            self, textvariable=self.name
        )  # , borderwidth=1, relief="solid")
        self.desc_label = ctk.CTkLabel(self, textvariable=self.desc)

        self.name_label.grid(column=0, row=0, padx=7, pady=7, sticky="ew")
        self.desc_label.grid(column=0, row=1, padx=7, pady=7, sticky="nsew")

        self.menu_frame = ctk.CTkFrame(self)

        self.menu_frame.grid(column=0, row=2, padx=7, pady=7, sticky="nsew")

        total_height = sum(
            widget.winfo_reqheight() + 5 for widget in self.winfo_children()
        )
        total_width = sum(widget.winfo_reqwidth() for widget in self.winfo_children())

        self.minsize(width=total_width, height=total_height)

        self.mainloop()


if __name__ == "__main__":
    game = Game()
    game.run()
