def main(z, x):
    a = (34*pow(x*x+z+pow(x, 3), 4)-pow(z, 2)/88)/(57*pow(z, 7)-65*pow(x, 4))
    b = (pow((z*z-z), 5)-25*(x/98-1))/(x-91*pow(abs(6*x*x+z/4+pow(x, 3)), 5))
    return a - b