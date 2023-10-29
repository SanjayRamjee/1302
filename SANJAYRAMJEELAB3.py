class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.x <= other.x:
            if self.y <= other.y:
                return True
            else:
                return False
        else:
            return False
    def __ge__(self, other):
        if self.x >= other.x:
            if self.y >= other.y:
                return True
            else:
                return False
        else:
            return False
    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        else:
            return False

loc1 =  Location(3, 4)
loc2 = Location(5, 8)
print(loc1 == loc2)
print(loc1 < loc2)
print(loc1 > loc2)