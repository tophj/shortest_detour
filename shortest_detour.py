"""
	shortest_detour.py
	By: Christopher Jones
	6/6/14

	Programming Challenge from lyft.com : "Calculate the detour distance between two different rides. Given four latitude / longitude 
	pairs, where driver one is traveling from point A to point B and driver two is traveling from 
	point C to point D, write a function (in your language of choice) to calculate the shorter of the 
	detour distances the drivers would need to take to pick-up and drop-off the other driver."

	Correct usage: 'python shortest_detour.py latt1 long1 latt2 long2 latt3 long3 latt4 long4'
	Where latt = Lattitude and long = Longitude

	ex. 'python shortest_detour.py 38.527618 -76.146819 37.421995 -122.084005 37.331741 -122.030333 37.783951 -122.407162'

	Return: None
	Prints out the correct response.

"""

from math import sin, cos, asin, sqrt, radians
import sys

# Determines the distance between two latt, long pairs using the haversine formula.
def distance(coordinate1, coordinate2):

	c1_latt = radians(coordinate1[0])
	c1_long = radians(coordinate1[1])
	c2_latt = radians(coordinate2[0])
	c2_long = radians(coordinate2[1])

	#earth_radius = 6378.1 # Kilometers
	earth_radius = 3959 # Miles

	latt_difference = (c2_latt - c1_latt)
	long_difference = (c2_long - c1_long)

	haversine = (sin(latt_difference / 2.0)**2) + (cos(c1_latt) * cos(c2_latt) * (sin(long_difference / 2.0)**2))
	total_distance = 2 * earth_radius * asin(sqrt(haversine))

	return total_distance


# Determines if it's shorter to driver 1 to pick up driver 2, drop him off, and then go to his destination, or the reverse.
def shortest_detour(driver1_start, driver1_end, driver2_start, driver2_end):

	d1_start = float(driver1_start[0]), float(driver2_start[1])
	d1_end  = float(driver1_end[0]), float(driver1_end[1])
	d2_start = float(driver2_start[0]), float(driver2_start[1])
	d2_end = float(driver2_end[0]), float(driver2_end[1])

	d1_picks_up_d2_distance = distance(driver1_start, driver2_start) + distance(driver2_start, driver2_end) + distance(driver2_end, driver1_end)
	d2_picks_up_d1_distance = distance(driver2_start, driver1_start) + distance(driver1_start, driver1_end) + distance(driver1_end, driver2_end)
	
	if(d1_picks_up_d2_distance < d2_picks_up_d1_distance):
		print "\nIt is shorter for driver 1 to pick up driver 2 by a distance of " + str(d2_picks_up_d1_distance - d1_picks_up_d2_distance) + " miles.\n"
	elif(d2_picks_up_d1_distance < d1_picks_up_d2_distance):
		print "\nIt is shorter for driver 2 to pick up driver 1 by a distance of " + str(d1_picks_up_d2_distance - d2_picks_up_d1_distance) + " miles.\n" 
	else:
		print "\nDetours for both drivers are equivalent in length.\n" 



if(len(sys.argv) != 9):
	print "\nIncorrect usage. Correct usage: 'python shortest_detour.py latt1 long1 latt2 long2 latt3 long3 latt4 long4'\n"


else:
	try:
		d1_start = float(sys.argv[1]), float(sys.argv[2])
		d1_end  = float(sys.argv[3]), float(sys.argv[4])
		d2_start = float(sys.argv[5]), float(sys.argv[6])
		d2_end = float(sys.argv[7]), float(sys.argv[8])

		shortest_detour(d1_start, d1_end, d2_start, d2_end)

	except ValueError:
		print "\nlatt and long should be numbers."
		print "Correct usage: 'python shortest_detour.py latt1 long1 latt2 long2 latt3 long3 latt4 long4'\n"
