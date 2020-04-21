from src.Dove import Dove


def get_parse(first_string, second_string):
    first_string = first_string.split()
    second_string = second_string.split()
    return {
        'count': first_string[0],
        'distance': first_string[1],
        'speeds': second_string
    }


def create_doves(count, distance, speeds):
    Dove.count = int(count)
    Dove.distance = int(distance)
    doves = []
    for index in range(Dove.count):
        doves.append(Dove(int(speeds[index]), index))
    return doves


def get_shift(doves_list):
    shift = 0
    for i in range(Dove.count):
        for j in range(Dove.count):
            if i < j and doves_list[i].time_of_way > doves_list[j].time_of_way:
                shift += 1
    return shift


def get_answer(first_string, second_string):
    data = get_parse(first_string, second_string)
    doves = create_doves(data['count'], data['distance'], data['speeds'])
    return get_shift(doves)



