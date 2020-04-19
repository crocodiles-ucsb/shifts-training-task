from src.get_shifts import get_shifts

# import argparse
#
#
# parser = argparse.ArgumentParser(description='Find shifts')
# parser.add_argument('-f', '--first string', type=str, help='Number of doves and distance')
# parser.add_argument('-S', '--second_string', type=str, help='Dove\'s speeds')
# args = parser.parse_args()


def task():
    str1 = input()
    str2 = input()
    shift = get_shifts(str1, str2)
    print(shift)


if __name__ == '__main__':
    task()
    # task(args.first_string, args.second_string)
    # print(get_shifts(args.first_string, args.second_string))
