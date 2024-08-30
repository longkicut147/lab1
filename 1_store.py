class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}    # item_name and its quantity

    @classmethod
    def from_size(cls, name, type, size):
        # create a new instance
        capacity = size * 50 // 100
        return cls(name, type, capacity)
    
    def add_item(self, item_name:str):
        self.items[item_name] = 0

        if self.items[item_name] < self.capacity:
            self.items[item_name] += 1
            return "{} added to the store".format(item_name)
        else:
            return "Not enough capacity in the store"
        
    def remove_item(self, item_name, amount):
        if item_name in self.items:
            if self.items[item_name] > 0:
                self.items[item_name] -= amount
                return "{} {} removed from the store".format(amount, item_name)
        else:
            return "Cannot remove {} {}".format(amount, item_name)
        
    def __repr__(self) -> str:
        return "{} of type {} with capacity {}".format(self.name, self.type, self.capacity)
    

first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)
print(first_store)
print(second_store)
print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
    