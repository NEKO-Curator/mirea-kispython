import math


def main(b, np, m, x):
    summation = 0
    for c in range(1, m+1):
        for i in range(1, np+1):
            for k in range(1, b+1):
                summation += 47*(math.sin(i)**4)-64*pow(x, 7)-pow(k-c*c, 3)
    return summation

#print(main(3, 7, 7, 0.44))