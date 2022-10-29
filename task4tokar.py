import math


def main(n):
    if n == 0:
        return 0.05
    if n>=1:
        return math.atan(main(n - 1))**3 - (math.ceil(main(n - 1)) / 68) - 18

if __name__ == '__main__':
    print(main(8))