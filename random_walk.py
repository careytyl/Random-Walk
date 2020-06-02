import matplotlib.pyplot as plt
from fill_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, s=15, edgecolors='none', cmap=plt.cm.Blues)
    plt.scatter(0, 0, s=100, c='green')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='red')

    plt.axis('off')

    plt.show()

    exit_loop = input("Run again? y/n: ")
    if exit_loop.lower() == 'n':
        break
