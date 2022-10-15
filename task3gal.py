def main(m, n):
    summation = 0
    for j in range(1, n+1):
        for k in range(1, m+1):
            summation += pow(k, 6)/57-83*k*k-pow((0.02+58*j*j+22*pow(j, 3)), 2)
    return summation

print(main(7, 8))