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
        self.current_room = self.first
        self.doors = [Door("Cupboard door", {1: 0, 0: 1})]

        self.places = [
            Thing(
                "Walk-in cupboard",
                items=[Thing("Pile of clothes", items=[Thing("Afikoman", action=win)])],
                places=[self.doors[0]],
            ),
            Thing(
                "Master bedroom",
                desc="As you look around the bedroom you see\n"
                + "a queen bed and a king bed\n"
                + "with a bedside table betweeen them,\n"
                + "a walk-in cupboard,\n"
                + "and several cardboard boxes.",
                places=[self.doors[0]],
            ),
        ]

    def run(self):
        self.title("Afikoman hunt")
        self.minsize(width=150, height=150)
        self.name = tk.StringVar(self, self.places[self.first].name)
        self.desc = tk.StringVar(self, self.places[self.first].desc)

        self.columnconfigure([0], weight=1)
        self.rowconfigure([1], weight=1)

        self.name_label = ctk.CTkLabel(self, textvariable=self.name)
        self.desc_label = ctk.CTkLabel(self, textvariable=self.desc, justify="center")

        self.name_label.grid(column=0, row=0, padx=7, pady=7, sticky="ew")
        self.desc_label.grid(column=0, row=1, padx=7, pady=7, sticky="nsew")

        self.menu_frame = ctk.CTkFrame(self)

        self.menu_frame.grid(column=0, row=2, padx=7, pady=7, sticky="nsew")
        self.menu_frame.columnconfigure([0], weight=1)

        total_height = sum(
            widget.winfo_reqheight() + 5 for widget in self.winfo_children()
        )
        total_width = sum(widget.winfo_reqwidth() for widget in self.winfo_children())

        self.minsize(width=total_width, height=total_height)

        # Menus
        self.open_menu = tk.Menu(self.menu_frame, tearoff=0)
        self.open_menubutton = ttk.Menubutton(
            self.menu_frame, text="Open", menu=self.open_menu, width=10
        )
        self.open_menubutton.grid(column=0, row=0, padx=7, pady=7)

        self.look_at_menu = tk.Menu(self.menu_frame, tearoff=0)
        self.look_at_menubutton = ttk.Menubutton(
            self.menu_frame, text="Look at", menu=self.look_at_menu, width=10
        )
        self.look_at_menubutton.grid(column=0, row=1, padx=7, pady=7)

        self.take_menu = tk.Menu(self.menu_frame, tearoff=0)
        self.take_menubutton = ttk.Menubutton(
            self.menu_frame, text="Take", menu=self.take_menu, width=10
        )
        self.take_menubutton.grid(column=0, row=2, padx=7, pady=7)

        self.gen_menus(self.places[self.current_room])

        self.mainloop()

    def open_door(self, door):
        pass

    def look_at(self, thing):
        pass

    def take_item(self, item):
        pass

    def gen_menus(self, thing):
        # current_place = self.places[self.first]
        if thing in self.places:
            if thing.desc:
                self.look_at_menu.add_command(
                    label="Surroundings", command=lambda item=thing: self.look_at(item)
                )

        if thing.items:
            for item in thing.items:
                if isinstance(item, Thing):
                    self.take_menu.add_command(
                        label=item.name, command=lambda item=item: self.take_item(item)
                    )
                if item.desc or item.items:
                    self.look_at_menu.add_command(
                        label=item.name, command=lambda item=item: self.look_at(item)
                    )
                # if self.menu.index("end") != 0:
                #    self.menu_frame.add_cascade(label=item.name, menu=self.menu)
        if thing.places:
            for place in thing.places:
                self.open_menu.add_command(
                    label=place.name, command=lambda door=place: self.open_door(door)
                )


if __name__ == "__main__":
    game = Game()
    game.run()
