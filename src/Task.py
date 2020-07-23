import argparse
import sys

from src.Shift import get_answer


def parse_args(args):
    parse = argparse.ArgumentParser(description='Find shifts')
    parse.add_argument(
        '-f', '--first_string', type=str, help='Number of doves and distance'
    )
    parse.add_argument('-s', '--second_string', type=str, help='Dove\'s speeds')
    return parse.parse_args(args)


if __name__ == '__main__':
    parser = parse_args(sys.argv[1:])
    print(get_answer(parser.first_string, parser.second_string))
