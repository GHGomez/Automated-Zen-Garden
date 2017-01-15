import coordinateshift as coor
import serial

arrarray = []
arrarray.append([coor.Coordinate(0.25, 0.25), coor.Coordinate(0.75, 0.75)
	, coor.Coordinate(0.25, 0.25)])

ser = serial.Serial('/dev/cu.usbmodemFA131', 9600)

for array in arrarray:
	for coordinate in array:
		ser.write(str(coordinate.c_1) + ' ')
		ser.write(str(coordinate.c_2) + '\n')
