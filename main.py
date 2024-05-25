from data import initialise_destinations_data
from population import Population
from route import spawn_from_parents
import config
import time
import random


def main():
    
    start_time = time.time()

    # Read in the destinations data and create a look-up table of distances between each for efficiency
    initialise_destinations_data()

    # Create an initial population of random routes
    current_population = Population()
    current_population.initialise_with_random_routes(config.POPULATION_SIZE)
    current_population.evaluate_and_sort_routes()

    for generation in range(1, config.GENERATIONS):
        print("Evolving generation", generation)
        new_population = evolve_new_population(current_population)

        new_population.evaluate_and_sort_routes()

        best_route = new_population.get_best_route()
        print(best_route.print_route("The best route is:"))

        print("Replacing the old population with the new one.")
        current_population = new_population

    # Say how long it took
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    print("Finished in", minutes, "minutes and", seconds, "seconds.")

def evolve_new_population(current_population):
    quickest_routes_in_current_population = get_best_subset_of_current_population(current_population)
    
    new_population = Population()
    while (new_population.get_size() < config.POPULATION_SIZE):
        # Pick two parents at random from the subset of quickest routes. We're allowed the same one
        parent_route_1 = current_population.get_route_at(random.randint(0, len(quickest_routes_in_current_population) - 1))
        parent_route_2 = current_population.get_route_at(random.randint(0, len(quickest_routes_in_current_population) - 1))

        child_route = spawn_from_parents(parent_route_1, parent_route_2)

        if random.random() < config.MUTATION_RATE:
            child_route.mutate()

        new_population.add_route(child_route)

    new_population.initialised = True
    return new_population
    
def get_best_subset_of_current_population(current_population):
    assert current_population.get_route_count() == config.POPULATION_SIZE, "Unexpected population size!"
    assert config.POPULATION_SUBSET_SIZE_THAT_CAN_REPRODUCE < config.POPULATION_SIZE, "Population subset size in the config file must be smaller than population size!"
    
    best_subset_of_current_population = current_population.get_best_subset_of_current_population(config.POPULATION_SUBSET_SIZE_THAT_CAN_REPRODUCE)
    assert len(best_subset_of_current_population) == config.POPULATION_SUBSET_SIZE_THAT_CAN_REPRODUCE, "Unexpected population subset size!"

    return best_subset_of_current_population

if __name__ == "__main__":
    main()