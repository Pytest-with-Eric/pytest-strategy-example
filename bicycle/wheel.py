class Wheel:
    def __init__(self, rim: float, tire: float):
        self.rim = rim
        self.tire = tire

    def diameter(self) -> float:
        """
        Query to calculate the diameter of the wheel
        """
        return round(self.rim + (self.tire * 2), 2)
