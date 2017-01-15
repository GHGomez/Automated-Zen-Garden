from __future__ import print_function
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
def coordinte_change(coro):
    L3 = ma.sqrt((coro.c_1 ** 2) + (coro.c_2 ** 2))
    rho = ma.atan((coro.c_1 ** 2) + (coro.c_2 ** 2))
    theta = rho + ma.acos(((L2 ** 2) + (L1 ** 2) - (L3 ** 2))/(-2 * L1 * L3))
    phi = ma.acos(((L3 ** 2) - (L2 ** 2) - (L1 ** 2))/(-2 * L1 * L2))
    return Coordinate(theta * 180 / ma.pi, phi * 180 / ma.pi)

newcor = cordinate_change(testcor)

print(newcor.c_1)
print(newcor.c_2)

def convert_corarray(corarray, filename):
	file = open(filename, 'w+')
	for coro in corarray:
		print(cordinate_change(coro), '\n', file= filename)

square_array = [Coordinate(0.5, 0.5), Coordinate(0.5, 0.5), 
Coordinate(0.5, 0.5), Coordinate(0.5, 0.5)]
		

