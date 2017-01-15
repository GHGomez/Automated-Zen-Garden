import coordinateshift as coor

squarearray = [coor.Coordinate(0.20, 0.20), coor.Coordinate(1, 0.20), 
coor.Coordinate(.80, .80), coor.Coordinate(0.20, 1), 
coor.Coordinate(0.20, 0.20)]

coor.convert_corarray(squarearray, 'squarearray.csv')

trianglearray = [coor.Coordinate(0.20, 0.20), coor.Coordinate(0.80, 0.20)
, coor.Coordinate(0.50, 0.80), coor.Coordinate(0.20, 0.20)]

coor.convert_corarray(trianglearray, 'trianglearray.csv')

stararray = [coor.Coordinate(0.30, 0.10), coor.Coordinate(0.50, 0.90),
coor.Coordinate(0.70, 0.10), coor.Coordinate(0.10, 0.60), 
coor.Coordinate(0.90, 0.60), coor.Coordinate(0.30, 0.10)]

coor.convert_corarray(stararray, 'stararray.csv')



