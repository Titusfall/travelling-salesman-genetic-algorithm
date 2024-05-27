from destination import Destination

import math

destinations = []
distances = {}

def initialise_destinations_data():
    print("Initialising...")

    # Example destination: London is longitude (x axis) -0.12 and latitude (y axis) 51.5.

    # It turns out that latitude and longitude aren't equal, due to the curviture of the Earth and Britain's northern position.
    # If you look at a map of the UK showing latitude and longitude, the grid squares are approximately twice as tall as they are wide.
    # If you treat them as equal and plot the UK cities on a grid, it squishes them the result vertically. Stretching the display graph
    # at the end wouldn't fix this properly, because it also affects the distances calculated. So we achieve a more accurate representation
    # by scaling the numbers when first inputting data. It's a fudge, but an important one in the UK cities test data.
    # With real data you wouldn't be calculating absolute distances at all, you'd read in actual distances and none of this would be necessary.
    scale_factor = 2

    add_destination("Aberdeen", -2.0943, 57.1497 * scale_factor, 0)
    add_destination("Belfast", -5.9301, 54.5973 * scale_factor, 1)
    add_destination("Birmingham", -1.8904, 52.4862 * scale_factor, 2)
    add_destination("Bradford", -1.7594, 53.795 * scale_factor, 3)
    add_destination("Bristol", -2.5879, 51.4545 * scale_factor, 4)
    add_destination("Cambridge", 0.1218, 52.2053 * scale_factor, 5)
    add_destination("Cardiff", -3.1791, 51.4816 * scale_factor, 6)
    add_destination("Coventry", -1.5197, 52.4068 * scale_factor, 7)
    add_destination("Derby", -1.4746, 52.9225 * scale_factor, 8)
    add_destination("Dundee", -2.9707, 56.462 * scale_factor, 9)
    add_destination("Edinburgh", -3.1883, 55.9533 * scale_factor, 10)
    add_destination("Glasgow", -4.2518, 55.8642 * scale_factor, 11)
    add_destination("Hull", -0.3274, 53.7676 * scale_factor, 12)
    add_destination("Leeds", -1.5491, 53.8008 * scale_factor, 13)
    add_destination("Leicester", -1.1398, 52.6369 * scale_factor, 14)
    add_destination("Liverpool", -2.9916, 53.4084 * scale_factor, 15)
    add_destination("London", -0.1278, 51.5074 * scale_factor, 16)
    add_destination("Manchester", -2.2426, 53.4808 * scale_factor, 17)
    add_destination("Newcastle", -1.6174, 54.9783 * scale_factor, 18)
    add_destination("Nottingham", -1.1581, 52.9548 * scale_factor, 19)
    add_destination("Oxford", -1.2544, 51.7548 * scale_factor, 20)
    add_destination("Plymouth", -4.1427, 50.3755 * scale_factor, 21)
    add_destination("Portsmouth", -1.0833, 50.8167 * scale_factor, 22)
    add_destination("Reading", -0.9781, 51.4543 * scale_factor, 23)
    add_destination("Sheffield", -1.4701, 53.3811 * scale_factor, 24)
    add_destination("Southampton", -1.4044, 50.9097 * scale_factor, 25)
    add_destination("Stoke-on-Trent", -2.1794, 53.0027 * scale_factor, 26)
    add_destination("Swansea", -3.9436, 51.6214 * scale_factor, 27)
    add_destination("Wolverhampton", -2.1266, 52.5862 * scale_factor, 28)
    add_destination("York", -1.0815, 53.959 * scale_factor, 29)

    calculate_distances()

def add_destination(name, x, y, id):
    new_destination = Destination(name, x, y, id)
    destinations.append(new_destination)

def calculate_distances():
    # Create a look-up table with the distance between every destination and every other destination,
    # for efficiency since we'll refer to it a lot. For this test data, just calculate the direct distance
    # between the two points as if roads weren't a thing. If using real data, it would be much better
    # to read in actual distance data instead of calculating it.
    for dest1 in destinations:
        for dest2 in destinations:

            if dest1 == dest2:
                distance = 0
            else:    
                distance = calculate_distance(dest1.x, dest1.y, dest2.x, dest2.y)
                
            key = (dest1.id, dest2.id)
            distances[key] = distance

def calculate_distance(x1, y1, x2, y2):
    x_diff_squared = (x2 - x1) ** 2
    y_diff_squared = (y2 - y1) ** 2
    distance = math.sqrt(x_diff_squared + y_diff_squared)
    return distance

def get_copy_of_destinations_list():
    # We can't just return the destinations list because then when we randomise the order it will affect the master list. So make a copy.
    # Note that we aren't cloning the destination items in the list, but that's okay because we never change them
    destinations_copy = []
    for dest in destinations:
        destinations_copy.append(dest)
    return destinations_copy

def get_number_of_destinations():
    return len(destinations)

def get_distance(dest1, dest2):
    key = (dest1.id, dest2.id)
    return distances[key]
