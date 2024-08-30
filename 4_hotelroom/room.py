class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guest = 0
        self.is_taken = False
    
    def take_room(self, people):
        if self.is_taken == False and self.capacity >= people:
            self.capacity += people
            self.is_taken = True
        else:
            return "Room number {} cannot be taken".format(self.number)
        
    def free_room(self):
        if self.is_taken == True:
            self.capacity = 0
            self.is_taken = False
        else:
            return "Room number {} is not taken".format(self.number)
        
    