import coordinateshift as coor
import serial

arrarray = []
arrarray.append([coor.Coordinate(0.25, 0.25), coor.Coordinate(0.75, 0.75)
	, coor.Coordinate(0.25, 0.25)])

ser = serial.Serial('/dev/cu.usbmodemFA131', 9600)

for array in arrarray:
	for coordinate in array:
		changed_coor = coor.coordinate_change(coordinate)
		ser.write(str(changed_coor.c_1) + ' ')
		ser.write(str(changed_coor.c_2) + '\n')
