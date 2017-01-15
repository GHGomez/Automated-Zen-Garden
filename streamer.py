import coordinateshift as coor
import serial

arrarray = []
arrarray.append([coor.Coordinate(0.25, 0.25), coor.Coordinate(0.75, 0.75)
	, coor.Coordinate(0.25, 0.25)])

ser = serial.Serial('/dev/ttyUSB0', 9600)

for array in arrarray:
	for coordinate in array:
		stringcor = str(coordinate)
		ser.write(bytes(coordinate))