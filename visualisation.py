import matplotlib.pyplot as plt
import route as Route
import destination as Destination

def display_as_graph(route):
    # Use the Matplotlib library to display a graph
    dest_names = []
    dest_xs = []
    dest_ys = []

    for destination in route.destinations:
        dest_names.append(destination.name)
        dest_xs.append(destination.x)
        dest_ys.append(destination.y)
        
    # Now add an additional element in the lists duplicating the starting position so we can connect back in a loop
    dest_names.append(dest_names[0])
    dest_xs.append(dest_xs[0])
    dest_ys.append(dest_ys[0])

    # Stretch the graph vertically to mirror the x2 scale factor in the data
    plt.figure(figsize=(3, 6))

    plt.scatter(dest_xs, dest_ys, color='blue', label='Places')

    number_of_unique_places = len(dest_xs) - 1

    for i in range(number_of_unique_places):
        plt.text(dest_xs[i], dest_ys[i], dest_names[i], fontsize=8, ha='right')

    # Don't show the ticks because the numbers aren't useful. 
    plt.xticks([])
    plt.yticks([])

    plt.plot(dest_xs, dest_ys, color='red', linestyle='-', linewidth=2)

    plt.show()
