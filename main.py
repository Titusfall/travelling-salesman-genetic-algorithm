from data import initialise_destinations_data
from population import Population
from route import spawn_from_parents
from visualisation import display_as_graph
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
    quickest_so_far = None
    gen_reached_optimum = None
    
    for generation in range(1, config.GENERATIONS):
        #print("Evolving generation", generation)
        new_population = evolve_new_population(current_population)

        new_population.evaluate_and_sort_routes()

        best_route = new_population.get_best_route()
        quickest_this_gen = best_route.get_total_distance()

        if quickest_so_far is None or quickest_this_gen < quickest_so_far:
            quickest_so_far = quickest_this_gen
            gen_reached_optimum = generation

        #best_route.print_route(f"Generation {generation}'s best route is:")
        print(f"Generation {generation}'s best route is {best_route.get_total_distance()}.")

        #print("Replacing the old population with the new one.")
        current_population = new_population

    # Say how long it took
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    print("Finished in", minutes, "minutes and", seconds, "seconds. Reached optimum solution in generation", gen_reached_optimum)

    display_as_graph(best_route)

def evolve_new_population(current_population):
    quickest_routes_in_current_population = get_best_subset_of_current_population(current_population)
    
    new_population = Population()
    while (new_population.get_size() < config.POPULATION_SIZE):
        # Pick two parents at random from the subset of quickest routes. We're allowed the same one
        parent_route_1 = current_population.get_route_at(random.randint(0, len(quickest_routes_in_current_population) - 1))
        parent_route_2 = current_population.get_route_at(random.randint(0, len(quickest_routes_in_current_population) - 1))

        child_route = spawn_from_parents(parent_route_1, parent_route_2)

        if random.random() < config.MUTATION_RATE:
            child_route.mutate(config.BIAS_TOWARDS_SWITCHING_NEIGHBOURS)

        new_population.add_route(child_route)

    new_population.initialised = True
    return new_population
    
def get_best_subset_of_current_population(current_population):
    assert current_population.get_route_count() == config.POPULATION_SIZE, "Unexpected population size!"
    assert config.PERCENTAGE_OF_POPULATION_THAT_CAN_REPRODUCE <= 1 and config.PERCENTAGE_OF_POPULATION_THAT_CAN_REPRODUCE > 0, "PERCENTAGE_OF_POPULATION_THAT_CAN_REPRODUCE in the config file must be between 0 and 1!"
    
    size_of_subset_that_can_reproduce = int(config.POPULATION_SIZE * config.PERCENTAGE_OF_POPULATION_THAT_CAN_REPRODUCE)
    assert size_of_subset_that_can_reproduce >= 2, "Invalid config settings - reproduction population too small!"

    best_subset_of_current_population = current_population.get_best_subset_of_current_population(size_of_subset_that_can_reproduce)
    
    return best_subset_of_current_population

if __name__ == "__main__":
    main()