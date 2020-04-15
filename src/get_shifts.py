from src.Dove import Dove


def get_shifts(first_string, second_string):
    first_string = first_string.split()
    second_string = second_string.split()
    Dove.count = int(first_string[0])
    Dove.distance = int(first_string[1])
    speeds = [int(speed) for speed in second_string]
    doves = []
    for index in range(Dove.count):
        doves.append(Dove(speeds[index], index))
    shift = 0
    for i in range(Dove.count):
        for j in range(Dove.count):
            if i < j and doves[i].time_of_way > doves[j].time_of_way:
                shift += 1
    return shift
