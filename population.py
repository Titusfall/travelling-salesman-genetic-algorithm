from route import Route

class Population():
    def __init__(self) -> None:
        self.routes = []
        self.initialised = False
        self.evaluated = False
        self.sorted = False

    def initialise_with_random_routes(self, size):
        for i in range(size):
            route = Route()
            route.randomise_destinations()
            self.routes.append(route)
            
        self.initialised = True
        print(len(self.routes), "random routes added to population")

    def add_route(self, route):
        self.routes.append(route)

    def get_size(self):
        return len(self.routes)
    
    def get_route_at(self, index):
        return self.routes[index]

    def evaluate_and_sort_routes(self):
        assert self.initialised == True, "Tried to evaluate population before initialising it!"
        assert self.evaluated == False, "Tried to evaluate population more than once!"
        assert self.sorted == False, "Tried to evaluate population that had somehow been sorted!"

        for route in self.routes:
            route.evaluate_route()
        
        self.evaluated = True

        self.sort_routes_by_shortest_distance()

    def get_best_subset_of_current_population(self, subset_size):
        assert self.evaluated == True, "Tried to get subset of population before they'd been evaluated!"
        assert self.sorted == True, "Tried to get subset of population before they'd been sorted!"
        return self.routes[:subset_size]

    def get_best_route(self) -> Route:
        if not self.sorted:
            self.sort_routes_by_shortest_distance()

        return self.routes[0]
    
    def sort_routes_by_shortest_distance(self):
        assert self.evaluated == True, "Tried to sort routes before they'd been evaluated!"
        assert self.sorted == False, "Tried to sort routes when they were already sorted!"

        self.routes.sort(key=lambda route: route.get_total_distance())
        self.sorted = True

    def get_route_count(self):
        return len(self.routes)

    def print_all_routes(self):
        print ("There are", len(self.routes), "routes:")
        for route in self.routes:
            route.print_route("")

