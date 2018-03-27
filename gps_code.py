import math
from math import cos, sin, atan2, sqrt


def main():
    print("Hello World!")

RAD = 3.14159265/180

def bearing_angle(lat1, long1, lat2, long2):
    long_diff = long2 * 3.14159265 / 180 - long1 * 3.14159265 / 180

    x = math.cos(lat2 * 3.14159265 / 180) * sin(long_diff)

    y = math.cos(lat1 * 3.14159265 / 180) * sin(lat2 * 3.14159265 / 180) - sin(lat1 * 3.14159265 / 180) * cos(lat2 * 3.14159265 / 180) * cos(long_diff)

    #x = sin(90 * 3.14159265 / 180);

    bearing = math.atan2(x, y)

    return bearing * 180 / 3.14159265


def distance(lat1, long1, lat2, long2):

	radius = 6371000;   #in metres

	#converting degrees to radians

	#calculating the diff of latitudes and longitudes

	long_diff = long2*3.14159265/180 - long1*3.14159265/180

	lat_diff = lat2*3.14159265/180 - lat1*3.14159265/180


	lat1 = lat1*3.14159265/180

	long1 = long1*3.14159265/180

	lat2 = lat2*3.14159265/180

	long2 = long2*3.14159265/180


	a = math.sin(lat_diff/2)*math.sin(lat_diff/2) + math.cos(lat1)*math.cos(lat2)*math.sin(long_diff/2)*math.sin(long_diff/2)
	c = 2*math.atan2(sqrt(a), math.sqrt(1-a))
	distance = radius*c


	return distance



if __name__ == "__main__":
    main()

    lat_1 = 37.305606
    long_1 = -121.892106
    lat_2 = 37.335507
    long_2 = -121.892106
    angle = bearing_angle(lat_1, long_1, lat_2, long_2)
    distance = distance(lat_1, long_1, lat_2, long_2)   #in meters

    print(angle)
    print(distance)

    heading = 0
    degree = angle - heading

    dir_msg = 0
    if ((0 < degree and degree <= 5) or (-360 <= degree and degree < -355)):
        dir_msg = 3 # go straight
    elif ((5 < degree and degree <= 15) or (-355 <= degree and degree < -345)):
        dir_msg = 2 # slight left: 5 degrees
    elif ((15 < degree and degree <= 60) or (-345 <= degree and degree < -300)):
        dir_msg = 1 # mid left: 15 degrees
    elif ((60 < degree and degree <= 180) or (-300 <= degree and degree < -180)):
        dir_msg = 0 # full left: 60 degrees
    elif ((355 < degree and degree <= 360) or (-5 <= degree and degree < 0)):
        dir_msg = 3 # go straight
    elif ((345 < degree and degree <= 355) or (-15 <= degree and degree < -5)):
        dir_msg = 4 # slight right: 5 degrees
    elif ((300 < degree and degree <= 345) or (-60 <= degree and degree < -15)):
        dir_msg = 5 # midright: 15degrees
    elif ((180 < degree and degree <= 300) or (-180 <= degree and degree <= -60)):
        dir_msg = 6 #full right: 60 degrees
    else:
        dir_msg = 7 # stop the motors, not able to calaculate correct angle to turn


    x = [10, 10, 4, 6]

    if x%2:
        print('hey')