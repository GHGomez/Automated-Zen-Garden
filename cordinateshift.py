import math as ma

L1 = 1
L2 = 1

#in rectangular as x,y and polar as theta phi
class Coordinate:
    def __init__(self, c_1, c_2):
        self.c_1 = c_1
        self.c_2 = c_2

testcor = Coordinate(ma.sqrt(0.5), ma.sqrt(0.5))

#Changes Coordinates from rectangular to dual polar
def cordinate_change(coro):
    L3 = ma.sqrt((coro.c_1 ** 2) + (coro.c_2 ** 2))
    rho = ma.atan((coro.c_1 ** 2) + (coro.c_2 ** 2))
    theta = rho + ma.acos(((L2 ** 2) + (L1 ** 2) - (L3 ** 2))/(-2 * L1 * L3))
    phi = ma.acos(((L3 ** 2) - (L2 ** 2) - (L1 ** 2))/(-2 * L1 * L2))
    return Coordinate(theta, phi)

newcor = cordinate_change(testcor)

print(newcor.c_1)
print(newcor.c_2)
