import coordinateshift as coor
import serial
import json
import requests
import time

cache = []
arrarray = []

ser = serial.Serial('/dev/cu.usbmodem411', 9600)

while(True):
    try:
        r = requests.get(
             "https://sheltered-tundra-18217.herokuapp.com/coordinates").json()
    except Exception as error:
        print(error)
        time.sleep(5)
        continue

    r['yaxis'].pop(0)

    coords = zip(r['xaxis'], r['yaxis'])

    if not len(cache) or not coords in cache:
        cache.append(coords)
    else:
        time.sleep(5)
        continue

    print cache
    for ar in cache:
        print ar
        for c in ar:
            changed_coor = coor.coordinate_change(coor.Coordinate(c[0], c[1]))
            print changed_coor
            ser.write(str(changed_coor.c_1) + ' ')
            ser.write(str(changed_coor.c_2) + '\n')
