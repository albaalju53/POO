import math

class Point():

    def move(self, x:float, y: float) -> None:
        self.x = x 
        self.y = y

    def reset(selft ) -> None:
        selft.move(0, 0)

    def calculate_distance( self, other: "Pont") -> float:
        return math.hypot( self.x - other.x, self.y - other.y)