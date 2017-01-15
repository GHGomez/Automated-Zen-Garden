#!/usr/bin/python
from __future__ import print_function
import math as ma
import sys

L1 = ma.sqrt(2)
L2 = ma.sqrt(2) / 2.0

#in rectangular as x,y and polar as theta phi
class Coordinate:
    def __init__(self, c_1, c_2):
        self.c_1 = c_1
        self.c_2 = c_2

#Changes Coordinates from rectangular to dual polar
def coordinate_change(coro):
    L3 = ma.sqrt((coro.c_1 ** 2) + (coro.c_2 ** 2))
    rho = ma.atan((coro.c_1 ** 2) + (coro.c_2 ** 2))
    theta = rho + ma.acos(((L2 ** 2) + (L1 ** 2) - (L3 ** 2))/(-2 * L1 * L3))
    phi = ma.acos(((L3 ** 2) - (L2 ** 2) - (L1 ** 2))/(-2 * L1 * L2))
    return Coordinate(theta * 180 / ma.pi, phi * 180 / ma.pi)

def convert_corarray(corarray, filename):
	file = open(filename, 'w+')
	for coro in corarray:
		print(coordinate_change(coro), '\n', file= filename)

def main(args):
    print(coordinate_change(Coordinate(int(args[0])), int(args[1])))

if __name__ == '__main__':
    main(sys.argv[1:])