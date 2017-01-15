import coordinateshift as coor
import serial
import json
import requests
import time

arrarray = []

ser = serial.Serial('/dev/cu.usbmodem621', 9600)

while(true):
	try:
        r = requests.get(
    	    "https://sheltered-tundra-18217.herokuapp.com/coordinates")
    
    except requests.ConnectionError, e:
    	print e
    	time.sleep(5)
    	continue

    arrarray.append(json.dump(r,skipkeys='NULL'))	
    for array in arrarray:
	    for coordinate in array
	        changed_coor = coor.coordinate_change(coordinate)
		    ser.write(str(changed_coor.c_1) + ' ')
		    ser.write(str(changed_coor.c_2) + '\n')
