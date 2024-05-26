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
    add_destination("Leeds", 1, 9, 5)
    add_destination("Birmingham", 2, 2, 6)
    add_destination("Bristol", 10, 6, 7)
    add_destination("Modbury", 0, 3, 8)
    add_destination("Plymouth", 5, 4, 9)
    add_destination("Newcastle", 11, 6, 10)
    add_destination("Derby", 6, 7, 11)
    add_destination("Glasgow", 7, 5, 12)
    add_destination("Swansea", 9, 5, 13)
    add_destination("Dublin", 3, 9, 14)
    add_destination("Exeter", 10, 1, 15)
    add_destination("York", 8, 9, 16)
    add_destination("Liverpool", 6, 0, 17)

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
