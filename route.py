
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

    def mutate(self):
        print ("Mutating... TODO")

    def get_total_distance(self):
        assert self.total_distance is not None, "get_total_distance() called before route evaluated!"
        return self.total_distance
    
    def get_length(self):
        return len(self.destinations)
    
    def get_destination_at(self, index):
        return self.destinations[index]

    def print_route(self, prefix):
        message = prefix

        # List the destinations
        for dest in self.destinations:
            message += f" {dest.name}"

        # And back to the beginning again
        message += f" ({self.destinations[0].name})"

        if self.total_distance is not None:
            message += f" - total distance of {self.total_distance}"
        else:
            message += " (route not yet evaluated)"

        print (message)

def spawn_from_parents(parent_route_1, parent_route_2):
    number_of_routes = parent_route_1.get_length()
    assert parent_route_2.get_length() == number_of_routes, "Parent routes are different lengths!"

    parent_route_1.print_route("Parent 1 is:")
    parent_route_2.print_route("Parent 2 is:")

    midpoint = random.randint(0, number_of_routes)
    #print ("Splitting parent routes at midpoint", midpoint)

    child_route = Route()

    # For the first half, we just copy the destinations from parent1 to the midpoint
    for i in range(midpoint):
        #print("Appending to child from parent 1 at position", i)
        child_route.destinations.append(parent_route_1.get_destination_at(i))        

    # For the second half, we can't just copy the parent2 destinations from the midpoint to the end because
    # then some destinations will be duplicated and some missed out. So instead we go through all of parent2
    # and just add those we haven't added yet
    for i in range(number_of_routes):
        #print("Appending to child from parent 2 at position", i)
        dest_in_parent2 = parent_route_2.get_destination_at(i)

        if dest_in_parent2 not in child_route.destinations:
            child_route.destinations.append(dest_in_parent2)

    assert child_route.get_length() == number_of_routes, "Child route is a different length!"

    child_route.print_route("Child is:")
    
    return child_route


    
