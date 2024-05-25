from data import initialise_destinations_data
from population import Population
from route import Route
import config
import time


def main():
    
    start_time = time.time()

    # Read in the destinations data and create a look-up table of distances between each for efficiency
    initialise_destinations_data()

    # Create an initial population of random routes
    current_population = Population()
    current_population.initialise_with_random_routes(config.POPULATION_SIZE)
    current_population.evaluate_routes()

    for generation in range(1, config.GENERATIONS):
        print("Evolving generation", generation)
        new_population = evolve_new_population(current_population)
        new_population.evaluate_routes()
        best_route = new_population.get_best_route()
        print("The best route is:")
        print(best_route.print_route())

    # Say how long it took
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    print("Finished in", minutes, "minutes and", seconds, "seconds.")

def evolve_new_population(current_population):
    new_population = Population()
    while (new_population.get_size() < config.POPULATION_SIZE):
        route = Route()
        route.randomise_destinations()
        new_population.add_route(route)

    new_population.initialised = True
    return new_population
    

if __name__ == "__main__":
    main()