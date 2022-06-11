import math
n = 2


def main(z, x):
    summation = 0
    for i in range(0, n):
        summation += 64 * pow(59 - 85 * pow(x[i], 2) - 14 * z[n
                              - math.ceil((i + 1) / 3)], 6)
    summation *= 87
    return summation
