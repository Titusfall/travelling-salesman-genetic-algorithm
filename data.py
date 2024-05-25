from destination import Destination

import math

destinations = []
distances = {}

def initialise_destinations_data():
    print("Initialising...")

    add_destination("Cardiff", 4, 12, 0)
    add_destination("Nottingham", 8, 2, 1)
    add_destination("London", 2, 0, 2)
    add_destination("Brighton", 1, 3, 3)
    add_destination("Edinburgh", 15, 5, 4)

    calculate_distances()

def add_destination(name, x, y, id):
    new_destination = Destination(name, x, y, id)
    destinations.append(new_destination)

def calculate_distances():
    for dest1 in destinations:
        for dest2 in destinations:

            if dest1 == dest2:
                distance = 0
            else:    
                distance = calculate_distance(dest1.x, dest1.y, dest2.x, dest2.y)
                #print("Distance between", dest1.name, "at", dest1.x, dest1.y, "and", dest2.name, "at", dest2.x, dest2.y, "is", distance)

            key = (dest1.id, dest2.id)
            distances[key] = distance

def calculate_distance(x1, y1, x2, y2):
    x_diff_squared = (x2 - x1) ** 2
    y_diff_squared = (y2 - y1) ** 2
    distance = math.sqrt(x_diff_squared + y_diff_squared)
    return distance

def get_number_of_destinations():
    return len(destinations)

def get_copy_of_destinations_list():
    # We can't just return the destinations list because then when we randomise the order it will affect the master list. So make a copy.
    # Note that we aren't copying the destination items in the list but that's okay because we never change them
    destinations_copy = []
    for dest in destinations:
        destinations_copy.append(dest)
    return destinations_copy


def get_distance(dest1, dest2):
    key = (dest1.id, dest2.id)
    return distances[key]
