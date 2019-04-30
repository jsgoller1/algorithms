class MazeGame():
    def create_maze(self):
        maze = Maze()
        room1 = Room(1)
        room2 = Room(2)
        door = Door(room1, room2)

        room1.set_side('N', Wall())
        room1.set_side('E', door)
        room1.set_side('S', Wall())
        room1.set_side('W', Wall())

        room1.set_side('N', Wall())
        room1.set_side('E', Wall())
        room1.set_side('S', Wall())
        room2.set_side('W', door)

        maze.add_room(Room(1))
        maze.add_room(Room(2))


class Maze():
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_no] = room

    def room_no(self, no):
        return self.rooms[no]


class MapSite():
    def enter(self):
        raise NotImplementedError


class Room(MapSite):
    def __init__(self, room_no):
        self.room_no = room_no
        self.sides = {'N': None,
                      'E': None,
                      'S': None,
                      'W': None}

    def enter(self):
        print("Now standing room {0}".format(self.room_no))
        return

    def set_side(self, side, target):
        if side not in self.sides:
            raise ValueError
        self.sides[side] = target

    def get_side(self, side):
        if side not in self.sides:
            raise ValueError
        return self.sides[side]


class Wall(MapSite):
    def enter(self):
        print("Ouch, my nose! I hit a wall.")
        return


class Door(MapSite):
    def __init__(self, room1=None, room2=None):
        self.room1 = room1
        self.room2 = room2
        self.is_open = False

    def enter(self):
        if self.is_open:
            print("Passing through a door...")
        else:
            print("Ouch! I banged my nose on a door. :(")
        return

    def other_side_from(self, side):
        if side not in [self.room1, self.room2]:
            raise ValueError
        else:
            return self.room1 if side == self.room2 else self.room2
