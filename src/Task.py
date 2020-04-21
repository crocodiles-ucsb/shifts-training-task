import argparse
from src.Shift import get_answer


parser = argparse.ArgumentParser(description='Find shifts')
parser.add_argument('-f', '--first_string', type=str, help='Number of doves and distance')
parser.add_argument('-s', '--second_string', type=str, help='Dove\'s speeds')
args = parser.parse_args()


if __name__ == '__main__':
    print(get_answer(args.first_string, args.second_string))
