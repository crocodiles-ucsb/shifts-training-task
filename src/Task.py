from src.get_shifts import get_shifts


def task():
    str1 = input()
    str2 = input()
    shift = get_shifts(str1, str2)
    print(shift)


if __name__ == '__main__':
    task()
