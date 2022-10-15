import math


def main(n, m, z):
    summation = 0
    for k in range(1, m+1):
        for i in range(1, n+1):
            summation += math.sqrt((z*z)/15)+math.acos(z)**7+16*pow((93*k*k+i), 3)
    return summation

print(main(3, 6, 0.58))