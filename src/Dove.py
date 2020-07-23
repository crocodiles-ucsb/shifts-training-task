class Dove:
    distance = 0
    count = 0

    def __init__(self, speed, number_of_dove):
        self.speed = speed
        self.number_of_dove = number_of_dove
        self.time_of_way = (Dove.distance / self.speed) + self.number_of_dove

    def __str__(self):
        return (
            f'Dove {self.number_of_dove} has speed {self.speed} km/min and '
            f'it will arrive in {self.time_of_way} minute'
        )
