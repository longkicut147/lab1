from room import Room

class Hotel:
    def __init__(self, name:str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")
    
    def add_room(self, room:str):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)
        return "can't take room"

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def print_status(self):
        print("Hotel {} has {} total guests".format(self.name, self.guests))
        free_rooms = [room.number for room in self.rooms if room.is_taken == False]
        taken_rooms = [room.number for room in self.rooms if room.is_taken == True]
        print("Free rooms: ", end="")
        print(", ".join(map(str, free_rooms)))
        print("Taken rooms: ", end="")
        print(", ".join(map(str, taken_rooms)))


hotel = Hotel.from_stars(5)
first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

hotel.print_status()