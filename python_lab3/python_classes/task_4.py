class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, second_point):
        return ((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2) ** 0.5

