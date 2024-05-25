
from data import get_copy_of_destinations_list, get_distance
import random

class Route():
    def __init__(self) -> None:
        self.destinations = []
        self.total_distance = None

    def randomise_destinations(self) -> None:
        self.destinations = get_copy_of_destinations_list()
        random.shuffle(self.destinations)

    def set_destinations(self, destinations) -> None:
        self.destinations = destinations
        
    def evaluate_route(self) -> None:
        self.total_distance = 0.0

        # Go through the list of destinations, looking up the distance of each step along the route,
        # including back to the beginning again
        for i in range(len(self.destinations)):
            if i == len(self.destinations) - 1:
                distance = get_distance(self.destinations[i], self.destinations[0])
            else:
                distance = get_distance(self.destinations[i], self.destinations[i+1])
            self.total_distance += distance

        #print ("Total distance of this route is", self.total_distance)

    def get_total_distance(self):
        assert self.total_distance is not None, "get_total_distance() called before route evaluated!"
        return self.total_distance

    def print_route(self):
        message = "Route order is:"

        # List the destinations
        for dest in self.destinations:
            message += f" {dest.name}"

        # And back to the beginning again
        message += f" {self.destinations[0].name}"

        if self.total_distance is not None:
            message += f" - total distance of {self.total_distance}"
        else:
            message += " (route not yet evaluated)"

        print (message)



    
