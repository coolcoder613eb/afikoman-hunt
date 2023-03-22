from classes import *
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox


class Game(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.first = 1  # starting room
        self.current_room = self.first
        self.doors = [
            Door(
                "Cupboard door",
                {1: 0, 0: 1},
                desc="This is the door to the walk-in cupboard.",
            )
        ]

        self.places = [
            Thing(
                "Walk-in cupboard",
                desc="You are in the walk-in cupboard.\n"
                + "As you look around the slightly cramped space,\n"
                + "You see mostly empty shelves\n"
                + "and some clothes hanging from\n"
                + "a rod on the wall.",
                items=[
                    Thing(
                        "Pile of clothes",
                        desc="These clothes must have fallen from the rod.",
                        items=[
                            Thing(
                                "Afikoman",
                                desc="This is the Afikoman you've been looking for.",
                                on_take=self.win,
                                # moveable=True,
                            )
                        ],
                    )
                ],
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

        self.menu_style = ttk.Style()

        self.menu_style.configure("menu_style.TMenubutton", font=(None, 14))

        self.name_label = ctk.CTkLabel(self, textvariable=self.name, font=(None, 22))
        self.desc_label = ctk.CTkLabel(
            self, textvariable=self.desc, font=(None, 18), justify="center"
        )

        self.name_label.grid(column=0, row=0, padx=7, pady=7, sticky="ew")
        self.desc_label.grid(column=0, row=1, padx=7, pady=7, sticky="nsew")

        self.menu_frame = ctk.CTkFrame(self)

        self.menu_frame.grid(column=0, row=2, padx=7, pady=7, sticky="nsew")
        self.menu_frame.columnconfigure([0], weight=1)

        total_height = sum(
            widget.winfo_reqheight() + 5 for widget in self.winfo_children()
        )
        total_width = sum(
            widget.winfo_reqwidth() + 5 for widget in self.winfo_children()
        )

        self.minsize(width=total_width, height=total_height)

        # Menus
        self.open_menu = tk.Menu(self.menu_frame, tearoff=0, font=(None, 14))
        self.open_menubutton = ttk.Menubutton(
            self.menu_frame,
            text="Open",
            menu=self.open_menu,
            width=10,
            style="menu_style.TMenubutton",
        )
        self.open_menubutton.grid(column=0, row=0, padx=7, pady=7)

        self.look_at_menu = tk.Menu(self.menu_frame, tearoff=0, font=(None, 14))
        self.look_at_menubutton = ttk.Menubutton(
            self.menu_frame,
            text="Look at",
            menu=self.look_at_menu,
            width=10,
            style="menu_style.TMenubutton",
        )
        self.look_at_menubutton.grid(column=0, row=1, padx=7, pady=7)

        self.take_menu = tk.Menu(self.menu_frame, tearoff=0, font=(None, 14))
        self.take_menubutton = ttk.Menubutton(
            self.menu_frame,
            text="Take",
            menu=self.take_menu,
            width=10,
            style="menu_style.TMenubutton",
        )
        self.take_menubutton.grid(column=0, row=2, padx=7, pady=7)

        self.gen_menus(self.places[self.current_room], True)

        self.mainloop()

    def show(self, text, action="", showcmd=True):
        self.desc.set(
            "\n".join(
                (
                    self.desc.get()
                    + "\n"
                    + (f"[{action}:]\n" if showcmd else "")
                    + text
                ).splitlines()[-20:]
            )
        )

    def open_door(self, door):
        if not door.locked:
            self.current_room = door.dest[self.current_room]
            self.name.set(self.places[self.current_room].name)
            self.show(
                self.look_at(self.places[self.current_room], show=False),
                f"Open {door.name}",
            )
            self.gen_menus(self.places[self.current_room], True)
        else:
            self.show(
                "That door is locked.",
                f"Open {door.name}",
            )

    def look_at(self, thing, showcmd=True, surr=False, show=True):
        desc = (
            "\n".join(
                (
                    thing.desc if thing.desc else "...",
                    *(f"There is a {x.name} here." for x in thing.items),
                )
            )
            if thing.items
            else thing.desc
        )
        if thing.items:
            self.gen_menus(thing)
        if show:
            self.show(
                desc,
                f"Look at {'Surroundings' if surr else thing.name}",
                showcmd=showcmd,
            )
        else:
            return desc

    def take_item(self, item):
        item.on_take()

    def win(self):
        self.show("***YOU WON***", "Take Afikoman")

    def is_in_menu(self, menu, name):
        last = menu.index(tk.END)
        last = last if last != None else 0
        for x in range(last + 1):
            if menu.entrycget(x, "label") == name:
                return True
        return False

    def gen_menus(self, thing, new=False):
        # current_place = self.places[self.first]
        if new:
            self.open_menu.delete(0, "end")
            self.look_at_menu.delete(0, "end")
            self.take_menu.delete(0, "end")
        if thing in self.places:
            if thing.desc:
                self.look_at_menu.add_command(
                    label="Surroundings",
                    command=lambda item=thing: self.look_at(item, surr=True),
                )

        if thing.items:
            for item in thing.items:
                if (
                    isinstance(item, Thing)
                    and item.moveable
                    and not self.is_in_menu(self.take_menu, item.name)
                ):
                    self.take_menu.add_command(
                        label=item.name, command=lambda item=item: self.take_item(item)
                    )
                if (item.desc or item.items) and not self.is_in_menu(
                    self.look_at_menu, item.name
                ):
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
                if place.desc:
                    self.look_at_menu.add_command(
                        label=place.name, command=lambda item=place: self.look_at(item)
                    )


if __name__ == "__main__":
    game = Game()
    game.run()
