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
            route.print_route()

        self.initialised = True
        print(len(self.routes), "random routes added to population")

    def add_route(self, route):
        self.routes.append(route)

    def get_size(self):
        return len(self.routes)

    def evaluate_routes(self):
        print("Evaluating population...")
        assert self.initialised == True, "Tried to evaluate population before initialising it!"

        for route in self.routes:
            route.evaluate_route()
        
        self.evaluated = True

    def get_best_route(self) -> Route:
        if not self.sorted:
            self.sort_routes_by_shortest_distance()

        return self.routes[0]
    
    def sort_routes_by_shortest_distance(self):
        assert self.evaluated == True, "Tried to sort routes before they'd been evaluated!"
        assert self.sorted == False, "Tried to sort routes when they were already sorted!"

        print ("Routes before sorting:")
        self.print_all_routes()

        self.routes.sort(key=lambda route: route.get_total_distance())
        self.sorted = True

        print ("Routes sorted by shortest distance:")
        self.print_all_routes()

    def print_all_routes(self):
        print ("There are", len(self.routes), "routes!")
        for route in self.routes:
            route.print_route()

