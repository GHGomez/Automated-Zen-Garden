import coordinateshift as coor

squarearray = [coor.Coordinate(0.01, 0.01), coor.Coordinate(1, 0.01), 
coor.Coordinate(1, 1), coor.Coordinate(0.01, 1), 
coor.Coordinate(0.01, 0.01)]

coor.convert_corarray(squarearray, 'squarearray.csv')

trianglearray = [coor.Coordinate(0.20, 0.20), coor.Coordinate(0.80, 0.20)
, coor.Coordinate(0.50, 0.80), coor.Coordinate(0.20, 0.20)]

coor.convert_corarray(trianglearray, 'trianglearray.csv')

resetarray = [coor.Coordinate(0.01, 0.01)]

coor.convert_corarray(resetarray, 'reset.csv')



