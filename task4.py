import math


def main(y):
    return{
        y == 0: 0.74,
        y == 1: 0.60,
        y >= 2: rec(y+1),
    }[True]


def rec(n):
    if(n == 1):
        return 0.74
    elif(n == 2):
        return 0.60
    else:
        return rec(n-1)+1+pow(1-rec(n-2), 2)
