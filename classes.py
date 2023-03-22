class Thing:
    def __init__(
        self,
        name,
        menu=None,
        desc=None,
        items=None,
        action=None,
        places=None,
        moveable=False,
    ):
        self.name = name  # for all
        self.menu = menu  # for item
        self.desc = desc  # for all (look)
        self.items = items  # for all (look)
        self.action = action  # for use
        self.places = places  # for place (go to)
        self.moveable = moveable  # for item (take)


class Door:
    def __init__(self, name, dest, desc=None, locked=False):
        self.name = name
        self.dest = dest
        self.desc = desc
        self.locked = locked
        self.items = False
