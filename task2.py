import math


def main(y):
    return{
        y < 159: pow(y, 5)/85-pow(y, 3)-75*y,
        159 <= y < 245: 32*y*y-pow(y*y-y*y*y/26, 7) - (y*y+10*y+y*y*y)/65,
        245 <= y < 270: pow(math.ceil(93*y-87*y*y), 3)/30+41*pow(y, 4),
        y >= 270: pow(y, 3)-pow(7*y+1, 5),
    }[True]




#print(main(158))
#     f(y) = \begin{cases}
# \frac{y^{5}}{85} - y^{3} - 75  y,& y < 159\\
# 32  y^{2} - \left(y^{2} - \frac{y^{3}}{26}\right)^{7} - \frac{y^{2} + 10  y + y^{3}}{65},& 159 \leq y < 245\\
# \frac{\left(\left\lceil 93  y - 87  y^{2} \right\rceil\right)^{3}}{30} + 41  y^{4},& 245 \leq y < 270\\
# y^{3} - \left(7  y + 1\right)^{5},& y \geq 270
# \end{cases}